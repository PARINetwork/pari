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

    $('.rich-text img').each(function() {
    	$(this).wrap('<a class="gallery" href="javascript:void(0)"></a>');
    });

    $('.rich-text .gallery').magnificPopup({
	type: 'image',
	tLoading: 'Loading image #%curr%...',
	image: {
	    titleSrc: function(item) {
		var el = item.el;
		return item.el.next("p").next("i");
	    }
	},
	gallery: {
	    enabled: true,
	    navigateByImgClick: true,
	    preload: [0,1] // Will preload 0 - before current, and 1 after the current image
	},
	callbacks: {
	    elementParse: function(item) {
		var $this = $(item.el).find("img");
		var src = $this.attr("data-original") || $this.prop("currentSrc") || $this.attr("src");
		item.src = src;
	    }
	}
    });
});
