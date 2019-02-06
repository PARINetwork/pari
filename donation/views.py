import base64
import hashlib
import hmac
import json
import logging
import time
import urllib

from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, \
    HttpResponseBadRequest, JsonResponse
from django.shortcuts import render, redirect
from django.utils.translation import ugettext_lazy as _
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from wagtail.wagtailcore.models import Site

from .helpers import DonationOptions
from .forms import DonateForm

logger = logging.getLogger(__file__)
razorpay_client = settings.RAZORPAY_CLIENT


def handle_instamojo_payment(form_data):
    pg_url = settings.INSTAMOJO["DONATE_URL"]
    params = {
        "data_name": form_data["name"],
        "data_email": form_data["email"],
        "data_phone": form_data["phone"],
        "data_Field_90444": form_data["pan"],
    }
    pg_url += "?{0}".format(urllib.urlencode(params))
    return HttpResponseRedirect(pg_url)


def create_razorpay_plan(amount, frequency):
    plan = razorpay_client.plan.create(data={
        'period': frequency.lower(),
        'interval': 1,
        'item': {
            'name': 'Plan B',
            'amount': int(amount) * 100,
            'currency': 'INR',
        }
    })
    return plan


def create_razorpay_subscription(plan_id, num_periods):
    subscription = razorpay_client.subscription.create(data={
        'plan_id': plan_id,
        'total_count': num_periods,
        'customer_notify': 0,
    })
    return subscription


def handle_razorpay_payment(form_data):
    if not razorpay_client:
        return HttpResponse(status=503)
    log_msg_prefix = "{0}|{1}|Rs.{2} | RZP ".format(form_data['email'],
                                                    form_data['name'],
                                                    form_data['amount'])
    logger.info(log_msg_prefix + "Initiating transaction")

    plan = create_razorpay_plan(form_data['amount'], form_data['frequency'])
    logger.debug(log_msg_prefix + "Created plan_id={0}".format(plan['id']))

    num_periods = settings.RAZORPAY['NUM_MONTHS_TO_RECUR'] \
                    if form_data['frequency'] == DonationOptions.Frequency.M \
                    else settings.RAZORPAY['NUM_YEARS_TO_RECUR']
    subscription = create_razorpay_subscription(plan['id'], num_periods)
    logger.debug(log_msg_prefix + "Created subscription_id={0}".format(subscription['id']))

    params = {
        'api_key': settings.RAZORPAY['API_KEY'],
        'subscription_id': subscription['id'],
        'amount': int(form_data['amount']) * 100,
        'customer_name': form_data['name'],
        'customer_phone': form_data['phone'],
        'customer_email': form_data['email'],
        'customer_pan': form_data["pan"],
        'timestamp': time.time()
    }
    checkout_url = reverse('razorpay_checkout')
    checkout_url += "?params={0}".format(base64.b64encode(json.dumps(params)))
    return redirect(checkout_url)


def donate_form(request):
    form = DonateForm()
    errors = None
    try:
        site = Site.objects.get(hostname=request.get_host())
    except Site.DoesNotExist:
        site = Site.objects.filter(is_default_site=True)[0]
    if request.method == "POST":
        form = DonateForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['frequency'] == DonationOptions.Frequency.ONE_TIME:
                return handle_instamojo_payment(form.cleaned_data)
            else:
                return handle_razorpay_payment(form.cleaned_data)

    return render(request, 'donation/donate_form.html', {
        "form": form,
        "errors": errors,
        "site": site,
        "current_page": 'donate_form',
    })


def donate_success(request):
    try:
        site = Site.objects.get(hostname=request.get_host())
    except Site.DoesNotExist:
        site = Site.objects.filter(is_default_site=True)[0]
    return render(request, 'donation/donate_success.html', {
        "site": site,
        "current_page": 'donate_success',
    })


def lower_first_item(item):
    return item[0].lower()


@csrf_exempt
@require_POST
def instamojo_webhook(request):
    status = 400
    data = request.POST.copy()
    hook_mac = data.pop("mac", [None])[0]
    keys = sorted(data.items(), key=lower_first_item)
    vals = "|".join([ii[1] for ii in keys])
    calc_mac = hmac.new(
        settings.INSTAMOJO["SALT"],
        vals,
        hashlib.sha1).hexdigest()
    if hook_mac == calc_mac:
        if data["status"] == "Credit":
            status = 200
            subject = _("Donation received")
            message = u""
            for (kk, vv) in data.items():
                message += unicode(kk) + u" : " + unicode(vv) + u"\r\n"
            send_mail(
                subject, message,
                settings.DEFAULT_FROM_EMAIL,
                settings.DONATE_EMAIL_RECIPIENTS
            )
    return HttpResponse("", status=status)


@never_cache
def razorpay_checkout(request):
    params = request.GET.get('params')
    if not params:
        return HttpResponseBadRequest()

    checkout_params = json.loads(base64.b64decode(params))

    current_timestamp, max_timestamp_delay = time.time(), 5.0
    if current_timestamp - checkout_params['timestamp'] > max_timestamp_delay:
        return HttpResponse("Link expired")

    log_msg_prefix = "{0}|{1}|Rs.{2} | RZP ".format(checkout_params['customer_email'],
                                                    checkout_params['customer_name'],
                                                    checkout_params['amount'] / 100)
    logger.info(log_msg_prefix +
                "Initiating Checkout for subscription_id={0}"
                .format(checkout_params['subscription_id']))

    return render(request, 'donation/razorpay_checkout.html', checkout_params)


@require_POST
def razorpay_verify(request):
    data = request.POST.copy()
    received_data_str = ', '.join(['{0}={1}'.format(k, v) for k, v in data.items()])
    logger.debug("RZP Received {0} for verification".format(received_data_str))

    expected_signature = hmac.new(
        key=settings.RAZORPAY['SECRET_KEY'],
        msg=data['razorpay_payment_id'] + '|' + data['subscription_id'],
        digestmod=hashlib.sha256
    ).hexdigest()

    if expected_signature != data['razorpay_signature']:
        logger.error("RZP Signature verification FAILED | subscription_id={0} | payment_id={1}"
                     .format(data['subscription_id'],
                             data['razorpay_payment_id']))
        return JsonResponse({'status': 'FAILED'})

    logger.debug("RZP Signature verification successful | subscription_id={0} | payment_id={1}"
                 .format(data['subscription_id'],
                         data['razorpay_payment_id']))
    logger.info("RZP Transaction successful | subscription_id={0} | payment_id={1}"
                .format(data['subscription_id'],
                        data['razorpay_payment_id']))
    return JsonResponse({'status': 'SUCCESS'})


@require_POST
def log_modal_close(request):
    data = request.POST.copy()
    logger.info("RZP User closed payment modal | {0}|{1} | {2}"
                .format(data['customer_name'],
                        data['customer_email'],
                        data['subscription_id']))
    return HttpResponse()