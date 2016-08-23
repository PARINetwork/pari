$(function() {
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 23, lng: 80},
        zoom: 4,
        styles: [
            {
                "elementType": "geometry.fill",
                "stylers": [
                    { "color": "#808080" },
                    { "visibility": "on" },
                    { "weight": 1 }
                ]
            },{
                "featureType": "administrative.country",
                "elementType": "geometry",
                "stylers": [
                    { "visibility": "on" },
                    { "color": "#000000" }
                ]
            },{
                "featureType": "administrative.province",
                "stylers": [
                    { "visibility": "on" },
                    { "color": "#000000" },
                    { "weight": 1 }
                ]
            },{
                "featureType": "water",
                "stylers": [
                    { "visibility": "on" },
                    { "color": "#000000" }
                ]
            },{
                "featureType": "road",
                "stylers": [
                    { "visibility": "off" }
                ]
            },{
                "featureType": "poi",
                "stylers": [
                    { "visibility": "off" }
                ]
            },{
                "featureType": "transit",
                "stylers": [
                    { "visibility": "off" }
                ]
            }
        ]
    });

    var markers = [];
    var location;
    for (var ii=0; ii < locations.length; ii++) {
	      location = locations[ii];
	      var marker = new google.maps.Marker({
            position: {lat: location.lat, lng: location.lng},
            map: map,
	          title: location.title
	      });
        marker.addListener('click', function() {
            var $this = this;
            var infoWindow = new google.maps.InfoWindow({
                content: $this.getTitle()
            });
            infoWindow.open(map, $this);
        });
        markers.push(marker);
    }

    var options = {
        imagePath: staticURL + 'map/images/m'
    };
    var markerCluster = new MarkerClusterer(map, markers, options);

    $('#filter').on('click', function() {
	      var checked = [];
	      $('input[name=filter]:checked').each(function() {
	          checked.push('filter=' + $(this).val());
	      });
	      if (checked.length > 0) {
	          window.location = '/map/?' + checked.join('&');
	      }
    });
});
