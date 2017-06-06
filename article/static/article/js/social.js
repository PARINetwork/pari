$(function () {
    if (('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch) {
        // Mobile device.
        $(".hidden.whatsapp").removeClass("hidden")
    }

    $('.arrow-wrap').on("click", function () {
        if ($(".arrow-collapse").hasClass("glyphicon-chevron-up"))
        {
            $(".arrow-collapse").removeClass("glyphicon-chevron-up").addClass("glyphicon-chevron-down");
        }else
        {
            $(".arrow-collapse").removeClass("glyphicon-chevron-down").addClass("glyphicon-chevron-up");
        }
    });
});