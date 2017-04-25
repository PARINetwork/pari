var Face = {
    init: function () {
        this._initPopup();
        this._initControls();
    },

    _popup: null,
    _sound: null,

    _initPopup: function () {
        this._popup = $('.popup-gallery').magnificPopup({
            delegate: '.mfp-image',
            type: 'image',

            tLoading: 'Loading image #%curr%...',
            mainClass: 'mfp-album-popup',

            gallery: {
                arrowMarkup: '<span title="%title%" class="mfp-arrow mfp-arrow-%dir%"><i class="fa fa-chevron-%dir% mfp-prevent-close slide-arrow"></i></span>',
                enabled: true,
                navigateByImgClick: true,
                preload: [0, 2],
            },

            image: {
                cursor: null,
                tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',

                titleSrc: $.proxy(function (item) {
                    var slideshow = this._popup.data('slideshow');
                    var icon = slideshow ? "pause" : "play";
                    var el = item.data.el;
                    return '<div>' +
                        el.attr('data-face-details') +
                        '</div>'
                }, this),

                markup: '<div class="mfp-figure">' +
                '<div class="mfp-close"></div>' +
                '<div class="mfp-img-holder">' +
                '<div class="mfp-img"></div>' +
                '</div>' +
                '<div class="mfp-bottom-bar">' +
                '<div class="mfp-title"></div>' +
                '<div class="mfp-counter"></div>' +
                '</div>' +
                '</div>'
            },
            closeBtnInside: true,
            callbacks: {
                updateStatus: $.proxy(function () {
                    this._initImage();
                }, this),
                close: $.proxy(function () {
                    this._popup.removeData('slideshow');
                    history.pushState(null, null, $(".popup-gallery").data("url"));
                    console.log("closed");
                    $(document).attr("overflow", "auto");
                }, this),
                open: function () {
                    var mfp = $.magnificPopup.instance;
                    var proto = $.magnificPopup.proto;

                    // extend function that moves to next item
                    mfp.next = function () {

                        // if index is not last, call parent method
                        if (mfp.index < mfp.items.length - 1) {
                            proto.next.call(mfp);
                            history.pushState(null, null, $($(".mfp-image")[mfp.index]).data("url"));
                        } else {
                            // otherwise do whatever you want, e.g. hide "next" arrow
                            proto.close();
                        }
                    };

                    // same with prev method
                    mfp.prev = function () {
                        if (mfp.index > 0) {
                            proto.prev.call(mfp);
                            history.pushState(null, null, $($(".mfp-image")[mfp.index]).data("url"));
                        }
                    };
                    $(document).attr("overflow", "hidden");
                }
            }
        });
        $.magnificPopup.instance.updateItemHTML = function () {
            var $this = this;
            var items = [];
            $.each($this.items, function (ii, item) {
                items.push({
                    src: $($("a.mfp-image")[ii]).attr("data-original-image-src"),
                    el: $($(".mfp-image")[ii])
                });
            });
            $this.items = items;
            $.magnificPopup.proto.updateItemHTML.call($this);
        }
    },


    _updateSlideshowButtonIcon: function () {
        var slideshow = this._popup.data('slideshow');
        var slideshowButton = $('.btn-slideshow i');
        if (slideshow) {
            slideshowButton.addClass('fa fa-pause');
            slideshowButton.removeClass('fa fa-play');
        } else {
            slideshowButton.addClass('fa fa-play');
            slideshowButton.removeClass('fa fa-pause');

        }

    },

    _initControls: function () {
        $('.album-controls').click($.proxy(function () {
            this._popup.data('slideshow', 'true');
            this._popup.magnificPopup('open');
        }, this));
    },

    _initImage: function () {
        $('.btn-fullscreen').on('click', function () {
            $('.mfp-container').addClass('mfp-container-fullscreen');
            return false;
        });

        $('.btn-slideshow').on('click', $.proxy(function () {
            var slideshow = this._popup.data("slideshow");
            if (slideshow) {
                this._popup.removeData('slideshow');
            } else {
                this._popup.data('slideshow', 'true');
            }

            this._updateSlideshowButtonIcon();

            return false;
        }, this));

        $('.mfp-figure').on('click', function () {
            $('.mfp-container').removeClass('mfp-container-fullscreen');
        });

        var mfp = $.magnificPopup.instance;
        history.pushState(null, null, $($(".mfp-image")[mfp.index]).data("url"));
    }

}

$(function () {
    Face.init();

    $(window).on("popstate", function () {
        $('a[data-url="' + location.pathname + '"]').click();
    });
});
