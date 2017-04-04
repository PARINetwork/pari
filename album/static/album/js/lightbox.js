var Album = {
    init: function() {
        // this._initSoundCloudWidget();
        this._initControls();
    },

    _popup: null,

    _initPopup: function(itemsData) {
        this._popup = $('.popup-gallery').magnificPopup({

            items: itemsData,

            tLoading: 'Loading image #%curr%...',

            mainClass: 'mfp-album-popup',

            gallery: {
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 2]
            },

            image: {
                cursor: null,
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',

                titleSrc: $.proxy(function (item) {
                    if(item.data.type == "image") {
                        var sideInfoTmpl = $.templates("#sideInfoTmpl");
                        var sideInfo = sideInfoTmpl.render(item.data);
                    }
                    return sideInfo;
                }, this),

                markup: $("#slide-template").html()
            },

            closeBtnInside: true,

            callbacks: {
                updateStatus: $.proxy(function () {
                    this._initImage();
                    // this._initAudio();
                }, this),
                markupParse: function(template, values, item) {
                    $(template).find('a.open-in-new-tab').attr('href', values.src);
                },
                change: function() {
                    if(this.currItem.data.type == "inline") {
                        var slideshowElement = this.content.find(".slide-show");
                        Album._initBackToAlbums(this.content.find(".back-to-albums"));
                        Album._initSlideShow(slideshowElement);
                        Album._updateSlideshowButtonIcon(slideshowElement);
                    }
                  },
                close: $.proxy(function () {
                    // this._stopWidget();
                    this._popup.removeData('slide-show');
                    clearInterval(this._popup.data('slide-show-timer'));
                }, this),

		open: function() {
		    var mfp = $.magnificPopup.instance;
		    var proto = $.magnificPopup.proto;

		    // extend function that moves to next item
		    mfp.next = function() {

			// if index is not last, call parent method
			if(mfp.index < mfp.items.length - 1) {
			    proto.next.call(mfp);
			} else {
			    // otherwise do whatever you want, e.g. hide "next" arrow
			    proto.close();
			}
		    };

		    // same with prev method
		    mfp.prev = function() {
			if(mfp.index > 0) {
			    proto.prev.call(mfp);
			}
		    };

		}
            }
        });
    },

    // _initSoundCloudWidget: function() {
    //     SC.initialize({
    //         client_id: "d129911dd3c35ec537c30a06990bd902"
    //     });
    // },

    // _player: null,
    // _reloadWidget: function(audio, autoplay) {
    // var $this = this;
    //     SC.stream("/tracks/" + audio).then(function(player) {
	 //    $this._player = player;
	 //    player.play();
	 //    player.on("finish", function() {
		// $this._onSoundFinish();
	 //    });
    // });
    // },

    // _toggleWidget: function() {
    // this._player.toggle();
    // this._togglePlayButton();
    // },

    _updateSlideshowButtonIcon: function (element) {
        var slideshow = this._popup.data('slide_show');
        if(slideshow) {
            $(element).addClass('fa-pause').removeClass('fa-play');
        } else {
            $(element).addClass('fa-play').removeClass('fa-pause');
        }
    },

    // _stopWidget: function() {
    // if (this._player) {
	 //    this._player.seek(0);
	 //    this._player.pause();
    // }
    // },

    // _onSoundFinish: function() {
    //     var slideshow = this._popup.data('slideshow');
    //     if(slideshow) {
    //         var magnificPopup = $.magnificPopup.instance;
    //         magnificPopup.next();
    //         return;
    //     }
    //     this._initPlayButton();
    // },

    _initControls: function() {
        $('.grid-container').click($.proxy(function (element) {

          var photoAlbum = $.templates("#photoAlbumTemplate");
          var photoAlbumHtml = photoAlbum.render({});
          $("#main_content").append(photoAlbumHtml);



             var slug = $(element.currentTarget).data('slug');
             $.get("/albums/"+slug+".json/", $.proxy(function(response) {
               this.generateCarousel(response);
            }, this));
         }, this));
    },

    generateCarousel: function(data) {
      this.carouselData = data;





      data.slides.forEach(function(slide, index) {
        slide.carouselPageClass = index === 0 ? "item image-container active" : "item image-container";
        var carouselPage = $.templates("#carouselPage");
        var carouselPageHtml = carouselPage.render(slide);
        $(".carousel-items").append(carouselPageHtml);
        $(".thumbnail-list").append('<li class="thumbnail left box"><img src='+slide.src+' /></li>');
      });



      data.authors.forEach(function(author) {
        var carouselAuthor = $.templates("#carouselAuthor");
        var carouselAuthorHtml = carouselAuthor.render(author);
        $(".carousel-items").append(carouselAuthorHtml);
      });

      $(".photo-album-popup").removeClass("hide");
      $(".carousel-container").addClass("carousel");
      $(".carousel-container").attr("data-ride", "carousel");

      // _initializeCarousel()
      handleCarouselEvents(this.carouselData);



    },
    _initializeCarousel: function(){

    },

    _constructAuthorItem: function(itemsJson){
        var authorTmpl = $.templates("#authorTmpl");
        var authors = authorTmpl.render(itemsJson['authors']);
        var authorSrc = $($("#author-template").html()).find("#author").append(authors).parent().html();
        var authorItem = {
            src: authorSrc,
            type: 'inline',
            show_title: false
        };
        return itemsJson['slides'].concat(authorItem);
    },

    _handleSlideShow: function (element) {
        var slideShow = this._popup.data("slide_show");
        if(slideShow) {
            this._pauseSlideShow(element);
        } else {
            this._playSlideShow(element);
        }
    },

    _playSlideShow: function (element) {
        $(element).addClass('fa-pause').removeClass('fa-play');
        this._popup.data('slide_show', 'true');
        var _this = this;
        var slideShowTimer = setInterval(function() {
            var slidePaused = !_this._popup.data('slide_show');
            if(slidePaused) {
                clearInterval(slideShowTimer);
            } else {
                $.magnificPopup.instance.next();
            }
        }, 3000);
        this._popup.data('slide-show-timer', slideShowTimer);
    },

    _pauseSlideShow: function (element) {
        $(element).addClass('fa-play').removeClass('fa-pause');
        this._popup.removeData('slide_show');
        clearInterval(this._popup.data('slide-show-timer'));
    },

    _dummy: function() {
        return {
                "slides": [
                {
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

            "authors": [
                {
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
    },

    _initImage: function() {
        // $('.btn-slideshow').on('click', $.proxy(function() {
        //     var slideshow = this._popup.data("slideshow");
        //     if(slideshow) {
        //        this._popup.removeData('slideshow');
        //     } else {
        //         this._popup.data('slideshow', 'true');
        //     }
        //     slideshow = this._popup.data("slideshow");
        //
        //     this._updateSlideshowButtonIcon();
        //     if(!this._player.isPlaying()) {
        //         this._initAudio();
        //     }
        //
        //     if(slideshow && !this._player.isPlaying()) {
        //         this._toggleWidget();
        //     }
        //
        //     return false;
        // }, this));
    },

    _initBackToAlbums: function(element) {
         $(element).on('click', function () {
           $.magnificPopup.close();
        });
    },

    _initSlideShow: function (element) {
        $(element).click($.proxy(function () {
           this._handleSlideShow(element);
        }, this));
    }

    // _initAudio: function() {
    //     var audio = $('.mfp-title .image-caption').data('audio');
    //     var controls = $('.mfp-controls');
    //     var slideshow = this._popup.data('slideshow');
    //
    //     if(audio && audio != "") {
    //         slideshow ? this._initPauseButton() : this._initPlayButton();
    //
    //         controls.show();
    //         controls.off('click');
    //         controls.on('click', $.proxy(this._toggleWidget, this));
    //
    //         this._reloadWidget(audio, slideshow);
    //     } else {
    //         controls.hide();
    //     }
    // },

    // _togglePlayButton: function() {
    //     $('.audio').toggle();
    // },
    //
    // _initPlayButton: function(){
    //     $('.fa-play', '.mfp-controls').show();
    //     $('.fa-pause', '.mfp-controls').hide();
    // },
    //
    // _initPauseButton: function(){
    //     $('.fa-play', '.mfp-controls').hide();
    //     $('.fa-pause', '.mfp-controls').show();
    // }
};

$(function() {
    Album.init();
});

function handleCarouselEvents(carouselData) {
  var totalItems = $('.carousel-items .item').length,
      currentIndex = 0,
      isPlaying = true;

  updateIndex();

  $("#carousel").carousel({
    interval: 2000,
    pause: false
  });

  $('#playPause').click(function() {
      isPlaying = !isPlaying;
      $(this).toggleClass("selected");
      $(this).removeClass("fa-play").removeClass("fa-pause");
      $(this).addClass(isPlaying ? "fa-play" : "fa-pause");
      $("#carousel").carousel(isPlaying ? "cycle" : "pause");
  });

  $('#showThumbnail').click(function() {
      toggleThumbnail();
  });

  // $('.show-slide-info').click(function () {
  //   $('.show-slide-info').toggleClass('fa-info-circle fa-chevron-circle-right');
  // })

  $('#showSlideInfo').click(function() {
      $(this).toggleClass("selected");
      $(".photo-album").toggleClass("show-slide-info");
  });

  $('.thumbnail-list li').click(function(event) {
    var index = $(event.currentTarget).index('.thumbnail-list li');
    $("#carousel").carousel(index);
      toggleThumbnail();
  });

  $('.close-thumbnail').click(function(event) {
    toggleThumbnail();
  });

  $('.back-to-albums').click(function(){
    $(".photo-album-popup").remove();
  })
  $('#carousel').on('slid.bs.carousel', function() {
      updateIndexOnSlide();
  });

  function updateIndexOnSlide() {
    currentIndex = getSelectedCarouselIndex();
    updateIndex();
  }

  function getSelectedCarouselIndex() {
    return $('.photo-album .carousel-items li.active').index('.photo-album .carousel-items li.item');
  }

  function updateIndex() {
    updateSlideInfo();
    totalItems = $('.carousel-items .item').length;
    $('.carousel-index').html((currentIndex + 1) + " / " + totalItems);
  }

  function updateSlideInfo() {
    if(currentIndex === totalItems - 1) {
      $(".slide-info .info").html("");
      return;
    }

    var data = carouselData.slides[currentIndex];
    if (currentIndex <= carouselData.slides.length ){
      $(".description").html(data.description);
      $(".album-title").text(data.album_title);
      $(".slide-photographer").text(data.slide_photographer.join(", "));
      $(".image-captured-date").text(data.image_captured_date);
      $(".slide-location").text(data.slide_location);
      $(".open-in-new-tab").attr("href", data.src);
    }

  }

  function toggleThumbnail() {
    $('#showThumbnail').toggleClass("selected");
    $(".photo-album").toggleClass("show-thumbnail");
  }

}
