$(function() {
    var map = L.map('map').setView(new L.LatLng(23, 80), 4);

    // add an OpenStreetMap tile layer
    L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    var markers = new L.MarkerClusterGroup();
    var location;
    for (var ii=0; ii < locations.length; ii++) {
	location = locations[ii];
	var marker = new L.marker(new L.LatLng(location.lat, location.lng), {
	    title: location.title,
	    alt: location.title
	}).bindPopup(location.title);
	markers.addLayer(marker);
    }
    map.addLayer(markers);

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
