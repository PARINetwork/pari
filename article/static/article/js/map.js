var map;
initMap=function(){
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7
    });

    var lat = $('.map-view').data("lat").toString().split(","),
        lng = $('.map-view').data("long").toString().split(",");
        content = $('.map-view').data("content").toString().split(",");

    for (var i = 0; i < lat.length; i++) {
        var pos = {lat: parseFloat(lat[i]), lng: parseFloat(lng[i])};
        map.setCenter(pos);
        var marker = new google.maps.Marker({
            map: map,
            position: pos,
        });
        var infowindow = new google.maps.InfoWindow({
        });
      google.maps.event.addListener(marker,'mouseover', (function(marker,content,infowindow){
            return function() {
                infowindow.setContent(content);
                infowindow.open(map,marker);
            };
        })(marker,content[i],infowindow));
    }
};

$(function() {
    initMap();
});
