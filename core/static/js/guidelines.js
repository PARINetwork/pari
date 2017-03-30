$(function() {
    $("a.index-link").on('click', function () {
        $("a.index-link").each(function () {
           $(this).removeClass('current-link');
        });
        $(this).addClass('current-link');
    });
});
