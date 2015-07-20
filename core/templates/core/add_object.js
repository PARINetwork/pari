function(modal) {
    {% block instance %}
    {% if instance %}
    $(function() {
	var instance = {"id": {{ instance.id }}, "name": "{{ instance.name }}"};
	modal.respond("objectAdded", instance);
	modal.close();
    });
    {% endif %}
    {% endblock %}

    $('form.add-object', modal.body).submit(function(ev) {
	ev.preventDefault();

        var formdata = $(this).serialize();

        $.ajax({
            url: this.action,
            data: formdata,
            type: 'POST',
	    dataType: 'text',
            success: function(response){
		modal.loadResponseText(response);
            }
        });
    });

}
