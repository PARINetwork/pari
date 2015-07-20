{% extends "core/add_object.js" %}

{% block instance %}
{% if instance %}
$(function() {
    var instance = {"id": {{ instance.id }}, "name": "{{ instance.name }}, {{ instance.district }}, {{ instance.state }} ({{ instance.point.x }}, {{ instance.point.y }})"};
    modal.respond("objectAdded", instance);
    modal.close();
});
{% endif %}
{% endblock %}
