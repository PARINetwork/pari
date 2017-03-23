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
                    if(item.data.show_title) {
                        // isCommentsAllowed = item.el.attr('data-allowcomments') == "True" ? true : false;
                        // var slideshow = this._popup.data('slideshow');
                        // var icon = slideshow ? "pause" : "play";
                        var returnedHTMLElement = '<div>' +
                            // '<h4 class="image-heading">' + item.el.attr('data-photographer') + '</h4>' +
                            // '<p class="image-date">' + item.el.attr('data-date') + '</p>' +
                            // '<p class="image-location">' + item.el.attr('data-location') + '</p>' +
                            '<p class="image-location-description"> description </p>';
                            // '<div class="image-caption" data-audio="' + item.el.attr('data-audio') + '">' + item.el.parent().find(".hidden").html() + '</div>' +
                            // '<div class="btn-toolbar">' +
                            // '<div class="btn-group">' +
                            // '<a class="btn btn-default btn-slideshow" href="#">Slideshow <i class="fa fa-' + icon + '"></i></a>' +
                            // '<a class="btn btn-default btn-fullscreen" href="#"><i class="fa fa-arrows-alt"></i></a>';

                        // if (isCommentsAllowed) {
                        //     returnedHTMLElement += '<a class="btn btn-default" id="disqus-comments-for-talking-albums" href="' + item.el.attr('data-url') + '"><i class="fa fa-share-square-o"></i></a>' +
                        //         '<a class="btn btn-default" href="' + item.el.attr('data-url') + '#comments"><i class="fa fa-comment-o"></i></a>';
                        // }

                        returnedHTMLElement += '</div>' +
                            '</div>' +
                            '</div>';
                    }
                    return returnedHTMLElement
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

    // _updateSlideshowButtonIcon: function () {
    //     var slideshow = this._popup.data('slideshow');
    //     var slideshowButton = $('.btn-slideshow i');
    //     if(slideshow) {
    //         slideshowButton.addClass('fa-pause');
    //         slideshowButton.removeClass('fa-play');
    //     } else {
    //         slideshowButton.addClass('fa-play');
    //         slideshowButton.removeClass('fa-pause');
    //     }
    // },

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
            // var slug = $(element.currentTarget).data('slug');
            // $.get("/albums/"+slug+".json/", $.proxy(function(response) {
                var slidesWithAuthor = this._constructAuthorItem(this._dummy());
                this._initPopup(slidesWithAuthor);
                this._popup.magnificPopup('open');
                this._playSlideShow();
                $('.mfp-container').addClass('mfp-container-fullscreen');
                $('.slide-show').click($.proxy(function () {
                   this._handleSlideShow();
                }, this));
            }, this));
        // }, this));
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

    _handleSlideShow: function () {
        var slideShow = this._popup.data("slide_show");
        if(slideShow) {
            this._pauseSlideShow();
        } else {
            this._playSlideShow();
        }
    },

    _playSlideShow: function () {
        $('.slide-show').addClass('fa-pause').removeClass('fa-play');
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

    _pauseSlideShow: function () {
        $('.slide-show').addClass('fa-play').removeClass('fa-pause');
        this._popup.removeData('slide_show');
        clearInterval(this._popup.data('slide-show-timer'));
    },

    _dummy: function() {
        return {
            slides: [
                {
                    src: '/static/img/stories-1.jpg',
                    type: 'image',
                    show_title: true
                }, {
                    src: '/static/img/stories-2.jpg',
                    type: 'image',
                    show_title: true
                }, {
                    src: '/static/img/stories-3-1.jpg',
                    type: 'image',
                    show_title: true
                }, {
                    src: '/static/img/stories-3-2.jpg',
                    type: 'image',
                    show_title: true
                }, {
                    src: '/static/img/stories-4.jpg',
                    type: 'image',
                    show_title: true
                }],

            authors: [
                {
                    // src: '.author',
                    // type: 'inline',
                    // show_title: false,
                    name: 'name1',
                    bio: 'bio1'
                },
                {
                    // src: '.author',
                    // type: 'inline',
                    // show_title: false,
                    name: 'name2',
                    bio: 'bio2'
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

        $('.popup-info').on('click', function() {
            $('.mfp-container').toggleClass('mfp-container-fullscreen');
            $('.popup-info').toggleClass('fa-info-circle fa-angle-right');
        });

        $('.back-to-albums').on('click', function () {
           $.magnificPopup.close();
        });
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
