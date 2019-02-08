from django.contrib import admin

from .models import RazorpayPlans


class RazorpayPlansAdmin(admin.ModelAdmin):
    list_display = ('plan_name', 'amount', 'frequency', 'plan_id',
                    'created_on', 'last_modified')
    readonly_fields = ('plan_name', 'amount', 'frequency', 'plan_id',
                       'created_on', 'last_modified')


admin.site.register(RazorpayPlans, RazorpayPlansAdmin)
