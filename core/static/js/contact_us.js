$(function() {
    $("select[name=category]").on("change", function() {
	$(".helpers div").each(function() {
	    $(this).addClass("hidden");
	});
	$(".form").addClass("hidden");
	if ($(this).children("option:selected").attr("class")) {
	    var klass = $(this).children("option:selected").attr("class");
	    $(".helpers ." + klass).removeClass("hidden");
	} else {
	    $(".form").removeClass("hidden");
	}
    });
    $(".helpers a.contact").on("click", function() {
	$(".form").removeClass("hidden");
    });
});
