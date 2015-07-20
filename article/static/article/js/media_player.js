$(function(){
    $("body").on("shown.bs.modal",  ".media-popup", function () {
        if($(this).data('video')) {
            var youtube_url = "http://www.youtube.com/embed/" + $(this).data('video') + "?autoplay=1";
            $('.video-container', this).html('<iframe src="' + youtube_url + '" frameborder="0" allowfullscreen></iframe>');

        } else {
            var soundcloud_url = "https://w.soundcloud.com/player/?url=http://api.soundcloud.com/tracks/" + $(this).data('audio');
            $('.audio-container', this).html('<iframe width="100%" height="166" scrolling="no" frameborder="no" src="' + soundcloud_url + '" frameborder="0"></iframe>');
        }
    });

    $("body").on('hidden.bs.modal', ".media-popup", function () {
        $('.video-container', this).html('');
        $('.audio-container', this).html('');
    });
});