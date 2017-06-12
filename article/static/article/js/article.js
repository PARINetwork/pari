var ArticleAlbum = {
    init: function () {
        this._initControls();
    },

    _initControls: function () {
        var articleAlbum = $.templates("#articleAlbumTemplate");
        var articleAlbumHtml = articleAlbum.render({});
        $("#main_content").append(articleAlbumHtml);
        this._generateCarousel(this._convertToJson());
    },

    _convertToJson: function () {

        console.log(this.getImageAndDescriptionOfRichtextImgHolder());
        return this.getImageAndDescriptionOfRichtextImgHolder();

    },

    getImageAndDescriptionOfRichtextImgHolder: function() {
        var self = this,
            jsonArray = [{
                src: this.getImageUrl($(".banner-container img")),
                description: "",
                article_title: $('#article-gallery-title').text(),
                id: 0
            }];

        $(".article-content .rich-text > .gallery, .article-content .rich-text > .rich-text-image-holder").each(function(index) {
            jsonArray.push({
                src: self.getImageUrl($(this).find("img")),
                description: self.getDescription(this),
                article_title: $('#article-gallery-title').text(),
                id: index + 1
            });
        });
        return jsonArray;
    },

    getImageUrl: function(img) {
        var src = $(img).attr('srcset') || $(img).attr('data-srcset');
        if (typeof src !== 'undefined') {
            return src.split(',')[1];
        }
        return $(img).attr('data-src') || $(img).attr('currentSrc') || $(img).attr('src');
    },

    getDescription: function(item) {
      var description = $(item).find("img").next("i").text().trim();
      if(!description) {
          description = $(item).find("img").parents(".gallery").next("i").text().trim();
      }
      if(!description) {
          $(item).nextAll(".center.paragraph-holder:not('.rich-text-image-holder')").each(function() {
              if(!description) {
                description = $(this).find("i").text().trim();
              }
          });
          $(item).nextAll("i:not('.rich-text-image-holder')").each(function() {
              if(!description) {
                description = $(this).find("i").text().trim();
              }
          });
      }
      return description;
    },
    
    _generateCarousel: function (data) {
        this.carouselData = data;
        data.forEach(function (slide, index) {
            slide.carouselPageClass = index === 0 ? "item image-container active" : "item image-container";
            var carouselPage = $.templates("#carouselPage");
            var carouselPageHtml = carouselPage.render(slide);
            $(".carousel-items").append(carouselPageHtml);
        });

        $("#carousel").carousel("pause");
        this.handleCarouselEvents(this.carouselData);
    },

    handleCarouselEvents: function (carouselData) {
        var totalItems = $('.carousel-items .item').length,
            currentIndex = 0;
        updateCurrentPageData();

        $('#showSlideInfo').click(function () {
            $(this).toggleClass("selected");
            $(this).removeClass("fa-angle-right").removeClass("fa-info-circle");
            $(this).addClass($(this).hasClass("selected") ? "fa-angle-right" : "fa-info-circle");
            $(".photo-album").toggleClass("show-slide-info");
        });

        $('.back-to-albums').click(function () {
            $(".carousel-container").removeClass("carousel");
            $(".photo-album-popup").addClass("hide");
        });

        $('#carousel').on('slid.bs.carousel', function () {
            updateIndexOnSlide();

        });

        $('.rich-text .gallery').click(function (event) {

            $(".photo-album-popup").removeClass("hide");
            $(".carousel-container").addClass("carousel");
            $(".carousel-container").attr("data-ride", "carousel");
            $("#carousel").carousel("pause");
            $("#carousel").carousel({
                interval: 0,
                pause: true
            });
            var index = $(event.currentTarget).attr('id');
            $("#carousel").carousel(parseInt(index) + 1);

        });

        $('.preview').on('click', function () {
            $("#carousel").carousel(0);
            $(".photo-album-popup").removeClass("hide");
            $(".carousel-container").addClass("carousel");
            $("#carousel").carousel("pause");
            $(".carousel-container").attr("data-ride", "carousel");

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
            $(".right-icons .open-in-new-tab").attr("href", data.src);

            if (currentIndex <= carouselData.length) {
                $(".slide-info .description").html(data.description);
                $(".slide-info .album-title").text(data.article_title);
            }
        }
    }

};

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


    $('.rich-text p, .rich-text h3, .rich-text h5').each(function () {
        if ($(this).find('img').length > 0) {
            $(this).addClass("rich-text-image-holder");
        } else {
            $(this).addClass("paragraph-holder");
        }
    });
    $('.rich-text img').each(function (index) {
        $(this).wrap('<a class="gallery" id=' + index + '></a>');
        $(this).parents('a').first().prepend('<i class="fa fa-expand fa-invert"></i>').css("position", "relative");
    });

    ArticleAlbum.init();

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
});
