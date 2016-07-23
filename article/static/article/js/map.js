$(function() {
    var map;
    window.initMap = function() {
        map = new google.maps.Map(document.getElementById('map'), {
            zoom: 7
        });
    }
    var lat = $('.map-view').data("lat").toString().split(","),
        lng = $('.map-view').data("long").toString().split(",");

    for (var i = 0; i < lat.length; i++) {
        map.setCenter([lat[i], lng[i]]);
        var marker = new google.maps.Marker({
            map: map,
            position: {lat: lat[i], lng: lng[i]}
        });
    }
});
