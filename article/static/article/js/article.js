$(function() {
    $(".scrollToTop").hide();

    $(".full-row .info a").on("click", function() {
	$("body").animate({
	    scrollTop: $(".article-title").offset().top
	}, 1000);
	$(".full-row .info").animate({
	    toggleClass: "hidden"
	}, 1000);
    });
    $(document).on("scroll", function() {
	if ($(window).scrollTop() < 10) {
	    $(".full-row .info").removeClass("hidden");
	    $(".scrollToTop").hide();
	} else {
	    $(".full-row .info").addClass("hidden");
	    $(".scrollToTop").show();
	}
    });

    $(".scrollToTop").on("click", function() {
	$("body").animate({
	    scrollTop: 0
	}, 1000);
    });
});
