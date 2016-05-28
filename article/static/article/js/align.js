// Temporary workaround until wagtail 1.5 is released
$(function() {
    $(".richtext").on("click", function() {
	      var $this = $(this);
	      $(".hallotoolbar .hallojustify button[title]").on("click", function() {
	          var selection = window.getSelection();
	          var block;
            if (selection.baseNode.tagName.toLowerCase() === "p") {
                block = selection.baseNode;
            } else {
                block = $(selection.baseNode).parents("p");
            }
	          var alignment = $(this).attr("title").toLowerCase();
	          $(block).removeClass("center left right justify");
	          $(block).addClass(alignment);
	          $this.trigger("hallomodified", [{content: $this.html()}]);
	          $this.addClass("isModified");
	      });
    });
});
