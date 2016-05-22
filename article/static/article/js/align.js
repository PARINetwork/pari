// Temporary workaround until wagtail 1.5 is released
$(function() {
    $(".richtext").on("click", function() {
	var $this = $(this);
	$(".hallotoolbar .hallojustify button[title]").on("click", function() {
	    var selection = window.getSelection();
	    var blockDisplayParent = $(selection.baseNode).parents("p");
	    var alignment = $(this).attr("title").toLowerCase();
	    $(blockDisplayParent).removeClass("center left right justify");
	    $(blockDisplayParent).addClass(alignment);
	    $this.trigger("hallomodified", [{content: $this.html()}]);
	    $this.addClass("isModified");
	});
    });
});
