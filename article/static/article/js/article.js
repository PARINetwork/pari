$(function () {
    $(".lazyload").css("display", "initial");

    $(".scrollToTop").hide();

    $(".full-row .info a").on("click", function () {
        $("body").animate({
            scrollTop: $(".article-title").offset().top
        }, 1000);
        $(".full-row .info").animate({
            toggleClass: "hidden"
        }, 1000);
    });
    $(document).on("scroll", function () {
        if ($(window).scrollTop() < 10) {
            $(".full-row .info").removeClass("hidden");
            $(".scrollToTop").hide();
        } else {
            $(".full-row .info").addClass("hidden");
            $(".scrollToTop").show();
        }
    });

    $(".scrollToTop").on("click", function () {
        $("body").animate({
            scrollTop: 0
        }, 1000);
    });


    $('.rich-text p').each(function () {
        if ($(this).find('img').length > 0) {
            $(this).addClass("rich-text-image-holder");
        } else {
            $(this).addClass("paragraph-holder");
        }
    });

    $('.rich-text img').each(function () {
        $(this).wrap('<a class="gallery" href="javascript:void(0)"></a>');
        $(this).parents('a').first().prepend('<i class="fa fa-expand fa-invert"></i>').css("position", "relative");
    });

    $('.rich-text .gallery').magnificPopup({
        type: 'image',
        tLoading: 'Loading image #%curr%...',
        image: {
            titleSrc: function (item) {
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
            elementParse: function (item) {
                var nextItem = $(this.items[this.index + 1]);
                $(nextItem).find("img").addClass("lazypreload");
                var $this = $(item.el).find("img");
                var src = $this.attr("data-src") || $this.prop("currentSrc") || $this.attr("src");
                item.src = src;
            }
        }
    });

    $('.preview').on('click', function (event) {
        alert("Hello its me!");
        var articleAlbum = $.templates("#articleAlbumTemplate");
        var articleAlbumHtml = articleAlbum.render({});
        $("#main_content").append(articleAlbumHtml);
        response = convertToJson();
        // var slug = $("div#slug-identifier").text();
        // $.get("/albums/" + slug + ".json/", $.proxy(function (response) {
        //     this.generateCarousel(response);
        // }, this));
        generateCarousel(response);
    });

    function convertToJson() {
        var jsonArray = [];
        $(".banner-container").each(function (index, item) {
           jsonArray.push({
               'srcset': $(item).find("img").attr('src'),
               'src': $(item).find("img").attr('src'),
               'description': '',
               'article_title': $('#article-gallery-title').text()
           });
       });

        $(".article-content .rich-text-image-holder").each(function (index, item) {
            var description = $(item).find("img").next("i").text().trim();
            jsonArray.push({
                'srcset': $(item).find("img").attr('srcset').toString().split(',')[1],
                'src': $(item).find("img").attr('src'),
                'description': description.length < 0 ? description : $(item).next(".center.paragraph-holder").find("i").text().trim(),
                'article_title': $('#article-gallery-title').text()
            });
        });
        return jsonArray;
    }

    function _dummy() {
        return [{
            "srcset": '/static/img/stories-1.jpg',
            "description": "Currently, image is being stored along with alt tags as single content. While doing this feature, we need to separate html & content. Hence we get the ability to add alt tags to images for SEO purposes",
            "album_title": "Weavers of walagpet"
        },
            {
                "srcset": '/static/img/stories-1.jpg',
                "description": "Currently, image is being stored along with alt tags as single content. While doing this feature, we need to separate html & content. Hence we get the ability to add alt tags to images for SEO purposes",
                "album_title": "Weavers of walagpet"
            }];
    }

    function generateCarousel(data) {
        this.carouselData = data;

        data.forEach(function (slide, index) {
            slide.carouselPageClass = index === 0 ? "item image-container active" : "item image-container";
            var carouselPage = $.templates("#carouselPage");
            var carouselPageHtml = carouselPage.render(slide);
            $(".carousel-items").append(carouselPageHtml);
        });

        $(".photo-album-popup").removeClass("hide");
        $(".carousel-container").addClass("carousel");
        $(".carousel-container").attr("data-ride", "carousel");

        handleCarouselEvents(this.carouselData);
    }
function handleCarouselEvents(carouselData) {
    var totalItems = $('.carousel-items .item').length,
        currentIndex = 0;

    updateCurrentPageData();


    $('#showSlideInfo').click(function () {
        $(this).toggleClass("selected");
        $(this).removeClass("fa-info-circle").removeClass("fa-angle-right");
        $(this).addClass($(this).hasClass("selected") ? "fa-angle-right" : "fa-info-circle");
        $(".photo-album").toggleClass("show-slide-info");
    });


    $('.back-to-albums').click(function () {
        $(".photo-album-popup").remove();
    });

    $('#carousel').on('slid.bs.carousel', function () {
        updateIndexOnSlide();

    });

    function updateIndexOnSlide() {
        currentIndex = getSelectedCarouselIndex();
        updateCurrentPageData();
    }

    function getSelectedCarouselIndex() {
        return $('.photo-album .carousel-items li.active').index('.photo-album .carousel-items li.item');
    }

    function updateCurrentPageData() {
        totalItems = $('.carousel-items .item').length;
        $('.carousel-index').html((currentIndex + 1) + " / " + totalItems);


        var data = carouselData[currentIndex];
        if (currentIndex <= carouselData.length) {
            $(".slide-info .description").html(data.description);
            $(".slide-info .album-title").text(data.article_title);
        }
    }
}
});
