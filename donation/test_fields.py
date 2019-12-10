from django.core.exceptions import ValidationError
from django.forms import forms
from django.test import SimpleTestCase

from .fields import AmountField, VALUE_ERROR_MSG

good_choices = (('1', 'aa'), ('2', 'bb'), ('Other', ''),)
bad_choices = (('1', 'aa'), ('2', 'bb'), ('3', 'cc'),)


class AmountFieldTests(SimpleTestCase):

    class AmountTestForm(forms.Form):
        amt = AmountField(choices=good_choices)

    @classmethod
    def setUpClass(cls):
        cls.field = AmountField(choices=good_choices)
        super(AmountFieldTests, cls).setUpClass()

    def test_last_choice_item_is_other(self):
        f1 = AmountField(choices=good_choices)
        with self.assertRaisesMessage(ValueError, VALUE_ERROR_MSG):
            f2 = AmountField(choices=bad_choices)

    def test_clean(self):
        self.assertEqual(self.field.clean(['1']), 1)
        self.assertEqual(self.field.clean(['Other', 10]), 10)
        with self.assertRaises(ValidationError):
            self.field.clean(['10'])

    def test_empty_other_is_disallowed(self):
        with self.assertRaises(ValidationError):
            self.field.clean(['Other', ''])
        with self.assertRaises(ValidationError):
            self.field.clean(['Other', None])

    def test_form_as_ul(self):
        form = self.AmountTestForm()
        self.assertHTMLEqual(form.as_ul(), u'<li><label for="id_amt_0">Amt:</label> <ul id="id_amt_0"><li><label for="id_amt_0_0"><input id="id_amt_0_0" name="amt_0" type="radio" value="1" /> aa</label></li>\n<li><label for="id_amt_0_1"><input id="id_amt_0_1" name="amt_0" type="radio" value="2" /> bb</label></li>\n<li><label for="id_amt_0_2"><input id="id_amt_0_2" name="amt_0" type="radio" value="Other" /> <input class="other-amount" id="id_amt_1" name="amt_1" onblur="this.placeholder=&#39;Other Amount&#39;" onfocus="this.placeholder=&#39;&#39;" placeholder="Other Amount" type="text" /></label></li></ul></li>')

    def test_form_cleaned_data(self):
        form = self.AmountTestForm({'amt_0': 'Other', 'amt_1': 100})
        form.is_valid()
        self.assertEqual(form.cleaned_data['amt'], 100)
        form = self.AmountTestForm({'amt_0': '1'})
        form.is_valid()
        self.assertEqual(form.cleaned_data['amt'], 1)
