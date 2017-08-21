from django.forms import SelectMultiple
from django.utils.safestring import mark_safe


class JqueryChosenSelectMultiple(SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        out = super(JqueryChosenSelectMultiple, self).render(name, value, attrs, choices)

        trigger_jquery_chosen = '''
        <script type="text/javascript">
            $("select[name={name}]").on("change", function() {{
                $(this).trigger("chosen:updated");
            }});
            $("select[name={name}]").chosen();
        </script>'''.format(name=name)

        return mark_safe(out + trigger_jquery_chosen)

    class Media:
        css = {
            'all': ('css/chosen.min.css',)
        }

        js = (
            'js/chosen.jquery.min.js',
        )
