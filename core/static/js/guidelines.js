$(function () {
    if (window.location.hash) {
        $("a[href='" + window.location.hash + "']").addClass("current-link");
        scrollToElement(window.location.hash);
    }

    $("a.index-link").on('click', function () {
        $("a.index-link").each(function () {
            $(this).removeClass('current-link');
        });
        $(this).addClass('current-link');
    });

    $(".guidelines-page a[href^='#']").on('click', function (e) {
        e.preventDefault();
        scrollToElement(this.hash);
        window.location.hash = this.hash
    });

    function scrollToElement(hash) {

        var parent = $('.guidelines-page .content'),
            childToScroll = $(hash);

        if ($(window).width() > 992) {
            $("html, body").animate({
                scrollTop: 0
            });
            parent.scrollTop(parent.scrollTop() - childToScroll.position().top - $("#header").height());
        }
        else {
            $("html, body").animate({
                scrollTop: childToScroll.offset().top - $("#header").height()
            });
        }
    }
});