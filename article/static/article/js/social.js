$(function(){
    var socialBar = $('.social');
    $.get('http://graph.facebook.com/?id=' + socialBar.data('url'), function(data) {
        $('.facebook .count', socialBar).html(data['shares']);
    })
    .fail(function() {
        $('.facebook .count', socialBar).html('0');
    });
    $.getJSON('http://urls.api.twitter.com/1/urls/count.json?callback=?', {'url': socialBar.data('url')}, function(data) {
        $('.twitter .count', socialBar).html(data['count']);
    })
    .fail(function() {
        $('.twitter .count', socialBar).html('0');
    });
    
});