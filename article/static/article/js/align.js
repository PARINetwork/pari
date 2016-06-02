// Temporary workaround until wagtail 1.5 is released
$(function() {
    $(".richtext").on("click", function() {
	      var $this = $(this);
	      $(".hallotoolbar .hallojustify button[title]").on("click", function() {
	          var selection = window.getSelection();
	          var block;
            if (selection.baseNode.nodeName === "#text") {
                block = $(selection.baseNode).parents("p");
            } else {
                block = selection.baseNode;
            }
	          var alignment = $(this).attr("title").toLowerCase();
	          $(block).removeClass("center left right justify");
	          $(block).addClass(alignment);
	          $this.trigger("hallomodified", [{content: $this.html()}]);
	          $this.addClass("isModified");
	      });
    });
});
