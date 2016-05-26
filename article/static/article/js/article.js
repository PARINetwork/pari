$(function() {
    $(".lazyload").css("display", "initial");

    $(".scrollToTop").hide();

    $(".full-row .info a").on("click", function() {
	$("body").animate({
	    scrollTop: $(".article-title").offset().top
	}, 1000);
	$(".full-row .info").animate({
	    toggleClass: "hidden"
	}, 1000);
    });
    $(document).on("scroll", function() {co
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
		var parent = item.el.closest("p");
		var sibling = parent.next("p");
		var ital = sibling.find("i");
		if (ital.length > 0 && ital.text().trim().length > 0) {
		    return sibling.html();
		} else {
		    return null;
		}
	    }
	},
	gallery: {
	    enabled: true,
	    navigateByImgClick: true,
	    preload: false
	},
	callbacks: {
	    elementParse: function(item) {
		var nextItem = $(this.items[this.index + 1]);
		$(nextItem).find("img").addClass("lazypreload");
	    	var $this = $(item.el).find("img");
	    	var src = $this.attr("data-src") || $this.prop("currentSrc") || $this.attr("src");
	    	item.src = src;
	    }
	}
    });
});
