$(function () {
    try {
        var map = L.map('map');
    }
     catch(e){
        return true;
    }
    var lat = $('.map-view').data("lat").toString().split(","),
        long = $('.map-view').data("long").toString().split(",");

    L.tileLayer('https://otile{s}-s.mqcdn.com/tiles/1.0.0/map/{z}/{x}/{y}.jpg', {
	subdomains: '1234',
        maxZoom: 7,
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors. '
	    + 'Tiles Courtesy of <a href="http://www.mapquest.com/" target="_blank">MapQuest</a>'
	    + '<img src="https://developer.mapquest.com/sites/default/files/mapquest/osm/mq_logo.png">'
    }).addTo(map);

    for (var i = 0; i < lat.length; i++) {
        map.setView([lat[i], long[i]], 6);
        L.marker([lat[i], long[i]]).addTo(map);
    }

});
