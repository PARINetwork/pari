$(function(){
    var socialBar = $('.social[data-url]');
    $.get('https://graph.facebook.com/?id=' + socialBar.data('url'), function(data) {
        $('.facebook .count', socialBar).html(data['shares']);
    })
    .fail(function() {
        $('.facebook .count', socialBar).html('0');
    });
    $.getJSON('https://urls.api.twitter.com/1/urls/count.json?callback=?', {'url': socialBar.data('url')}, function(data) {
        $('.twitter .count', socialBar).html(data['count']);
    })
    .fail(function() {
        $('.twitter .count', socialBar).html('0');
    });
    
});
