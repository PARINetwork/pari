function addObject(obj, elem) {
    ModalWorkflow({
	      url: "/admin/" + obj + "/add/",
		  onload: {
			  'chooser': function(modal, jsonData) {
				if(jsonData['result']){
					$(function() {
					  modal.respond("objectAdded", jsonData['result']);
					  modal.close();
				  });
				}
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
			  },
		  },
	      responses: {
	          objectAdded: function(data) {
		            var widget = $(elem);
		            widget.prepend('<option value="' + data.id + '" selected="selected">' + data.name + '</option>');
		            $(widget).trigger("change");
	          }
	      },
    });
}
