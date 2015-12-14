function addObject(obj, elem) {
    ModalWorkflow({
	url: "/admin/" + obj + "/add/",
	responses: {
	    objectAdded: function(data) {
		var widget = $(elem);
		widget.prepend('<option value="' + data.id + '" selected="selected">' + data.name + '</option>');
		$(widget).trigger("change");
	    }
	}
    });
}
