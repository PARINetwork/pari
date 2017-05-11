$(function () {
    if (!window.location.hash) {
        window.location.hash = '#section-1-1';
    }
    $("a[href='" + window.location.hash + "']").addClass("current-link");
    scrollToElement(window.location.hash);


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
        $("html, body").animate({
            scrollTop: 0
        });
        var parent = $('.guidelines-page .content'),
            childToScroll = $(hash);
        parent.scrollTop(parent.scrollTop() + childToScroll.position().top);
    }
});