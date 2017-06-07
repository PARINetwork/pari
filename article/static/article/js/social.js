$(function () {
    if (('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch) {
        // Mobile device.
        $(".hidden.whatsapp").removeClass("hidden")
    }

    $('.glyphicon-chevron-up').onclick(function () {
        $(".arrow-collapse").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
    });

    $('.glyphicon-chevron-down').onClick( function () {
        $(".arrow-collapse").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
    });
});