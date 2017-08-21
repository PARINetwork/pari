from django.forms import SelectMultiple
from django.utils.html import format_html
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


class JqueryChosenSelectMultipleWithAddObject(JqueryChosenSelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        out = super(JqueryChosenSelectMultipleWithAddObject, self).render(name, value, attrs, choices)
        obj = name.split('-')[-1]

        obj_add_button = format_html('''
        <div class="addbutton">
            <a href="javascript:void(0);" onclick="addObject('{obj}', 'select[name={name}]');"
            class="button bicolor icon icon-plus">Add {obj}</a>
        </div>''', obj=obj, name=name)

        return mark_safe(out + obj_add_button)

    class Media:
        js = (
            'js/add_object.js',
        )
