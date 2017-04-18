var Album = {
    init: function () {
        this._initControls();
    },

    stopAudioPlayer: function () {
        if (this._player) {
            this._player.seek(0);
            this._player.pause(0);
            this._player.dispose();
        }
    },

    playAudio: function () {
      if(this._player) {
          this._player.play();
      }
    },

    pauseAudio: function () {
        if(this._player) {
            this._player.pause();
        }
    },

    prepareSoundCloudWidget: function (trackId) {
        var isTalkingAlbum = $("div#type-identifier").text() === "talking_album";
        if(isTalkingAlbum) {
          $("#playPause").hide();
        } else {
          $("#playPause").show();
        }


        var mediaPlayer = new MediaPlayerControl(".audio-player-controls");
        if (this._player) {
            this._player.seek(0);
            this._player.play();
        }

        SC.initialize({
            client_id: "d129911dd3c35ec537c30a06990bd902"
        });
        var $this = this;
        SC.stream(trackId).then(function (player) {
            $this._player = player;
            player.play();

            player.on("time", function () {
                mediaPlayer.updateOnSeek(player.currentTime(), player.options.duration);
            });

            player.on("state-change", function (e) {
                if (e === "playing") {
                    mediaPlayer.setVolume(player.getVolume());
                }
            });

            player.on("finish", function () {
                $("#carousel").carousel("next");
            });

            $(".audio-player-controls").on("play-pause-click", function (event, state) {
                if(state.isPaused) {
                  Album.pauseAudio();
                } else {
                  Album.playAudio();
                }
            });

            $(".audio-player-controls").on("volume-seekbar-click", function (event, data) {
                player.setVolume(data.volume / 100);
            });

            $(".audio-player-controls").on("volume-seekbar-drag", function (event, data) {
                player.setVolume(data.volume / 100);
            });

            $(".audio-player-controls").on("seeker-seekbar-click", function (event, data) {
                var seekTime = player.options.duration * data.seekPercent / 100;
                player.seek(seekTime);
                player.play(seekTime);
            });

            $(".audio-player-controls").on("seeker-seekbar-drag", function (event, data) {
                var seekTime = player.options.duration * data.seekPercent / 100;
                player.seek(seekTime);
                player.play(seekTime, player);
            });

            $('#carousel').on('slid.bs.carousel', function () {
              Album.playAudio();
              mediaPlayer.play();
            });


        });
    },

    _initControls: function () {
        var photoAlbum = $.templates("#photoAlbumTemplate");
        var photoAlbumHtml = photoAlbum.render({});
        $("#main_content").append(photoAlbumHtml);
        var type = $("div#type-identifier").text();
        if (type == 'talking_album') {
            $(".volume-control").removeClass("hidden");
            $(".seek-bar-control").removeClass("hidden");
        }
        var slug = $("div#slug-identifier").text();
        $.get("/albums/" + slug + ".json/", $.proxy(function (response) {
            this.generateCarousel(response);
        }, this));
    },

    generateCarousel: function (data) {
        this.carouselData = data;

        data.slides.forEach(function (slide, index) {
            slide.carouselPageClass = index === 0 ? "item image-container active" : "item image-container";
            var carouselPage = $.templates("#carouselPage");
            var carouselPageHtml = carouselPage.render(slide);
            $(".carousel-items").append(carouselPageHtml);

            if (index === 0) {
                var carouselInfoBox = $.templates("#carouselStartingIntro");
                var carouselInfoBoxHtml = carouselInfoBox.render(slide);

                $(".carousel-items .item:first-child .wrapper").append(carouselInfoBoxHtml);
                if ($("div#type-identifier").text() == "talking_album") {
                    var trackId = slide.track_id;
                    Album.prepareSoundCloudWidget("/tracks/"+trackId);
                }
            }

            $(".thumbnail-list").append('<li class="thumbnail left box"><img src=' + slide.src + ' /></li>');
        });

        data.authors.forEach(function (author) {
            var carouselAuthor = $.templates("#carouselAuthor");
            var carouselAuthorHtml = carouselAuthor.render(author);
            $(".carousel-items").append(carouselAuthorHtml);
        });

        $(".photo-album-popup").removeClass("hide");
        $(".carousel-container").addClass("carousel");
        $(".carousel-container").attr("data-ride", "carousel");

        // _initializeCarousel()
        handleCarouselEvents(this.carouselData);
        setTimeout(function () {
            positionFloatingText();
        }, 500);

        $(window).resize(function () {
            positionFloatingText();
        });

    },

    _initializeCarousel: function () {

    },

    _dummy: function () {
        return {
            "slides": [{
                "src": '/static/img/stories-1.jpg',
                "type": 'image',
                "description": "Currently, image is being stored along with alt tags as single content. While doing this feature, we need to separate html & content. Hence we get the ability to add alt tags to images for SEO purposes",
                "album_title": "Weavers of walagpet",
                "slide_photographer": "vinod",
                "image_captured_date": "20 May 2017",
                "slide_location": "Madurai"
                // }, {
                //     src: '/static/img/stories-2.jpg',
                //     type: 'image',
                // }, {
                //     src: '/static/img/stories-3-1.jpg',
                //     type: 'image',
                // }, {
                //     src: '/static/img/stories-3-2.jpg',
                //     type: 'image',
            }, {
                "src": '/static/img/stories-4.jpg',
                "type": 'image',
                "description": "Featured image is random. Should have an option to select one. Featured image is random. Should have an option to select one. ",
                "album_title": "Weavers of walagpet",
                "slide_photographer": "deepthi",
                "image_captured_date": "30 May 2017",
                "slide_location": "Chennai"
            }],

            "authors": [{
                // src: '.author',
                // type: 'inline',
                // show_title: false,
                "name": 'name1',
                "bio": 'bio1'
            },
                {
                    // src: '.author',
                    // type: 'inline',
                    // show_title: false,
                    "name": 'name2',
                    "bio": 'bio2'
                }
            ]
        }
    }
};

$(function () {
    Album.init();
});

function positionFloatingText() {
    if ($(".floating-text").length === 0) {
        return;
    }
    var image = $('.carousel-items .item:first-child img');
    var contentHeight = image.get(0).offsetHeight * 0.4,
        contentWidth = image.get(0).offsetWidth * 0.5;

    contentHeight = contentHeight < 245 ? 245 : contentHeight;
    contentWidth = contentWidth < 415 ? 415 : contentWidth;

    var top = image.get(0).offsetTop + (image.get(0).offsetHeight - contentHeight) / 2;


    $(".floating-text").css({
        left: image.get(0).offsetLeft + (image.get(0).offsetLeft * 0.15) + 40,
        top: top,
        height: contentHeight,
        width: contentWidth

    });
}

function handleCarouselEvents(carouselData) {
    var totalItems = $('.carousel-items .item').length,
        currentIndex = 0,
        isTalkingAlbum = $("div#type-identifier").text() === "talking_album",
        isSlideshowPlaying = !isTalkingAlbum;

    updateCurrentPageData();

    $("#carousel").carousel({
        interval: isTalkingAlbum ? 1000 * 60 : 5000,
        pause: isTalkingAlbum
    });

    if(isTalkingAlbum) {
        $("#carousel").carousel("pause");
    }

    $('#playPause').click(function () {
        isSlideshowPlaying ? pauseSlide() : playSlide();
        $(this).toggleClass("selected");
    });

    $('#showThumbnail').click(function () {
        toggleThumbnail();
    });

    // $('.show-slide-info').click(function () {
    //   $('.show-slide-info').toggleClass('fa-info-circle fa-chevron-circle-right');
    // })

    $('#showSlideInfo').click(function () {
        $(this).toggleClass("selected");
        $(this).removeClass("fa-info-circle").removeClass("fa-angle-right");
        $(this).addClass($(this).hasClass("selected") ? "fa-angle-right" : "fa-info-circle");
        $(".photo-album").toggleClass("show-slide-info");

        setTimeout(function () {
            positionFloatingText();
        }, 500);
    });

    $('.thumbnail-list li').click(function (event) {
        var index = $(event.currentTarget).index('.thumbnail-list li');
        $("#carousel").carousel(index);
        toggleThumbnail();
        if(isSlideshowPlaying) {
            playSlide();
        }
    });

    $('.close-thumbnail').click(function (event) {
        toggleThumbnail();
        if (isSlideshowPlaying === true){
            playSlide();
        }
    });

    $('.back-to-albums').click(function () {
        Album.stopAudioPlayer();
    });

    function pauseSlide() {
        isSlideshowPlaying = false;
        $('#playPause').removeClass("fa-play").addClass("fa-pause");
        $("#carousel").carousel("pause");
    }

    function playSlide() {
        isSlideshowPlaying = true;
        $('#playPause').removeClass("fa-pause").addClass("fa-play");
        $("#carousel").carousel("cycle");
    }

    $('#carousel').on('slid.bs.carousel', function () {
        if ($("div#type-identifier").text() == "talking_album") {
            pauseSlide();
        }
        updateIndexOnSlide();
        if ($("div#type-identifier").text() == "talking_album") {
            var data = carouselData.slides[currentIndex];
            var trackId = data.track_id;
            Album.prepareSoundCloudWidget("/tracks/"+trackId);
        }
        if (currentIndex === 0) {
            setTimeout(function () {
                positionFloatingText();
            }, 500);
        }
    });

    function updateIndexOnSlide() {
        currentIndex = getSelectedCarouselIndex();
        updateCurrentPageData();
    }

    function getSelectedCarouselIndex() {
        return $('.photo-album .carousel-items li.active').index('.photo-album .carousel-items li.item');
    }

    function updateCurrentPageData() {
        updateSlideInfo();
        totalItems = $('.carousel-items .item').length;
        $('.carousel-index').html((currentIndex + 1) + " / " + totalItems);
        $(".thumbnail-list li").removeClass("selected");
        $(".thumbnail-list li:nth-child(" + (currentIndex + 1) + ")").addClass("selected");
    }

    function updateSlideInfo() {
        if (currentIndex === totalItems - 1) {
            $(".slide-info .info").html("");
            return;
        }

        var data = carouselData.slides[currentIndex];
        if (currentIndex <= carouselData.slides.length) {
            $(".slide-info .description").html(data.description);
            $(".slide-info .album-title").text(data.album_title);
            $(".slide-info .slide-photographer").text(data.slide_photographer.join(", "));
            $(".slide-info .image-captured-date").text(data.image_captured_date);
            $(".slide-info .slide-location").text(data.slide_location);
            $(".slide-info .open-in-new-tab").attr("href", data.src);
        }

    }

    function toggleThumbnail() {
        $('#showThumbnail').toggleClass("selected");
        $(".photo-album").toggleClass("show-thumbnail");
    }
}
