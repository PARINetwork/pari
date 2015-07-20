function addObject(obj) {
    ModalWorkflow({
	url: "/admin/" + obj + "/add/",
	responses: {
	    objectAdded: function(data) {
		var widget = $("#id_" + obj);
		widget.prepend('<option value="' + data.id + '">' + data.name + '</option>');
		widget.find("option").first().attr("selected", "selected");
		$(widget).trigger("change");
	    }
	}
    });
}
