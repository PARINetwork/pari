var Album = {
    init: function () {
        this._initControls();
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
                slide.photographerNames = slide.slide_photographer.map(function(i) { return i.trim()}).join(", ");
                var carouselInfoBoxHtml = carouselInfoBox.render(slide);
                $(".carousel-items .item:first-child .wrapper").append(carouselInfoBoxHtml);
                if ($("div#type-identifier").text() == "talking_album") {
                    var trackId = slide.track_id;
                    Album.prepareSoundCloudWidget("/tracks/"+trackId);
                }
                var albumDescription = slide.album_description;
                if(albumDescription.length > 450) {
                  albumDescription = albumDescription.substring(0, 450);
                }
                $(".floating-text .description").html(albumDescription);
            }

            $(".thumbnail-list").append('<li class="thumbnail left box"><img src=' + slide.src + ' /></li>');
        });

        data.authors.forEach(function (author) {
            var url = "";
            if (location.protocol != 'https:') {
                url = "http://"+window.location.hostname+author.author_url;
            } else {
                url = "https://"+window.location.hostname+author.author_url;
            }
            var fbShare = "https://facebook.com/sharer.php?u="+url;
            var twitterShare = "https://twitter.com/intent/tweet?url="+url+"&amp;hashtags=RuralIndiaOnline";
            author["fbShare"] = encodeURI(fbShare);
            author["twitterShare"] = encodeURI(twitterShare);
            author["url"] = encodeURI(url);
        });

        var carouselAuthor = $.templates("#carouselAuthor");
        var carouselAuthorHtml = carouselAuthor.render({"authors": data.authors});
        $(".carousel-items").append(carouselAuthorHtml);

        $(".photo-album-popup").removeClass("hide");
        $(".carousel-container").addClass("carousel");
        $(".carousel-container").attr("data-ride", "carousel");

        handleCarouselEvents(this.carouselData);
        setTimeout(function () {
            positionFloatingText();
        }, 500);

        $(window).resize(function () {
            positionFloatingText();
        });
    },

    prepareSoundCloudWidget: function (trackId) {
        var isTalkingAlbum = $("div#type-identifier").text() === "talking_album";
        if(isTalkingAlbum) {
          $("#playPause").hide();
        } else {
          $("#playPause").show();
        }

        var mediaPlayer = new MediaPlayerControl(".audio-player-controls");

        SC.initialize({
            client_id: "d129911dd3c35ec537c30a06990bd902"
        });
        var $this = this;

        SC.stream(trackId).then(function (player) {
            if (player.options.protocols[0] === 'rtmp') {
                player.options.protocols.splice(0, 1);
            }
            player.play();

            $this._player = player;
            if(isTalkingAlbum) {
              $(".play-pause")
              .removeClass("fa-play fa-pause selected")
              .addClass("fa-pause");
            }

            $this._player.on("time", function () {
                mediaPlayer.updateOnSeek(player.currentTime(), player.options.duration);
            });

            $this._player.on("state-change", function (e) {
                if (e === "playing") {
                    mediaPlayer.setVolume(player.getVolume());
                }
            });

            $this._player.on("finish", function () {
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
                $this._player.setVolume(data.volume / 100);
            });

            $(".audio-player-controls").on("volume-seekbar-drag", function (event, data) {
                $this._player.setVolume(data.volume / 100);
            });

            $(".audio-player-controls").on("seeker-seekbar-click", function (event, data) {
                var seekTime = player.options.duration * data.seekPercent / 100;
                $this._player.seek(seekTime);
                $this._player.play(seekTime);
                $(".play-pause").removeClass("fa-play fa-pause selected").addClass("fa-pause");
            });

            $(".audio-player-controls").on("seeker-seekbar-drag", function (event, data) {
                var seekTime = player.options.duration * data.seekPercent / 100;
                $this._player.seek(seekTime);
                $this._player.play(seekTime, player);
                $(".play-pause").removeClass("fa-play fa-pause selected").addClass("fa-pause");
            });

            $('#carousel').on('slid.bs.carousel', function () {
              Album.stopAudioPlayer();
              Album.playAudio();
              mediaPlayer.play();
            });


        });
    },

    stopAudioPlayer: function () {
        if (this._player) {
            this._player.seek(0);
            this._player.pause(0);
            this._player.dispose();
            this._player = null;
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

    var imageHeight = image.get(0).offsetHeight,
        contentHeight = imageHeight * 0.4,
        contentWidth = image.get(0).offsetWidth * 0.5;

    contentHeight = contentHeight < 350 ? 350 : contentHeight;
    contentHeight = contentHeight > imageHeight ? imageHeight : contentHeight;
    contentWidth = contentWidth < 415 ? 415 : contentWidth;
    var top = image.get(0).offsetTop + (imageHeight - contentHeight) / 2;

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
        $(".play-pause").show();
    } else {
      $(".play-pause").hide();
    }

    $('#playPause').click(function () {
        isSlideshowPlaying ? pauseSlide() : playSlide();
        $(this).toggleClass("selected");
    });

    $('#showSlideInfo').click(function () {
        $(this).toggleClass("selected");
        $(this).removeClass("fa-info-circle").removeClass("fa-angle-right");
        $(this).addClass($(this).hasClass("selected") ? "fa-angle-right" : "fa-info-circle");
        $(".photo-album").toggleClass("show-slide-info");

        setTimeout(function () {
            positionFloatingText();
        }, 500);
    });

    $('#showThumbnail').click(function () {
        pauseSlide();
        toggleThumbnail();
        $(".thumbnail-list li").removeClass("selected");
        $(".thumbnail-list li:nth-child(" + (currentIndex + 1) + ")").addClass("selected");
    });

    $('.thumbnail-list li').click(function (event) {
        var index = $(event.currentTarget).index('.thumbnail-list li');
        $("#carousel").carousel(index);
        toggleThumbnail();
        playSlide();
    });

    $('.close-thumbnail').click(function (event) {
        toggleThumbnail();
        playSlide();
    });

    $('.back-to-albums').click(function () {
        Album.stopAudioPlayer();
    });

    function pauseSlide() {
        isSlideshowPlaying = false;
        $('#playPause').removeClass("fa-pause").addClass("fa-play");
        $("#carousel").carousel("pause");
    }

    function playSlide() {
        isSlideshowPlaying = true;
        $('#playPause').removeClass("fa-play").addClass("fa-pause");
        $("#carousel").carousel("cycle");
    }

    $('#carousel').on('slid.bs.carousel', function () {
        if ($("div#type-identifier").text() == "talking_album") {
            pauseSlide();
        }
        updateIndexOnSlide();
        if ($("div#type-identifier").text() == "talking_album") {
            var data = carouselData.slides[currentIndex];
            if(data) {
              var trackId = data.track_id;
              Album.prepareSoundCloudWidget("/tracks/"+trackId);
              $(".audio-player-controls").show();
            } else {
              Album.stopAudioPlayer();
              $(".audio-player-controls").hide();
            }

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
        if(currentIndex === carouselData.slides.length) {
          if(!$(".carousel-area").hasClass("author-page")) {
              $(".carousel-area").addClass("author-page");
          }
        } else {
          $(".carousel-area").removeClass("author-page");
        }


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
            $(".slide-info .slide-photographer").text(data.slide_photographer.map(function(i) { return i.trim()}).join(", "));
            $(".slide-info .image-captured-date").text(data.image_captured_date);
            $(".slide-info .slide-location").text(data.slide_location);
            $(".open-in-new-tab").attr("href", data.src);
        }

    }

    function toggleThumbnail() {
        $('#showThumbnail').toggleClass("selected");
        $(".photo-album").toggleClass("show-thumbnail");
    }
}
