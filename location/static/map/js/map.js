var MapPage = {

  borderStroke: "#747474",

  createMap: function(mapElement, config) {
    this.mapInstance = new google.maps.Map(mapElement, {
        center: config.center,
        zoom: config.zoom,
        styles: this.getStyles()
    });

    this.createMarkerClusters();
    this.handleEvents();
    this.handleResize();
    this.highlightDefault();
  },

  handleResize: function() {
    var _this = this;
    google.maps.event.addDomListener(window, "resize", function() {
       var center = _this.mapInstance.getCenter();
       google.maps.event.trigger(_this.mapInstance, "resize");
       _this.mapInstance.setCenter(center);
    });
  },

  createMarkerClusters: function() {
    new MarkerClusterer(this.mapInstance, this.getMarkers(), {
        imagePath: staticURL + 'map/images/m'
    });
  },

  getMarkers: function() {
    var map = this.mapInstance;
    return locations.map(function(location, index) {
      var marker = new google.maps.Marker({
          position: {lat: location.lat, lng: location.lng},
          map: map,
          title: location.title
      });
      marker.addListener('click', function() {
          var infoWindow = new google.maps.InfoWindow({
              content: this.getTitle()
          });
          infoWindow.open(map, this);
      });
      return marker;
    });
  },

  highlightDefault() {
      this.updateStateDistrict($(".toggler li:first-child").text().trim().toLowerCase());
  },

  handleEvents: function() {
    var self = this;
    $(".toggler li").on("click", function() {
      if(!$(this).hasClass("selected")) {
        $(".toggler li").removeClass("selected");
        $(this).addClass("selected");
        self.updateStateDistrict($(this).text().trim().toLowerCase());
      }
    });
  },

  updateStateDistrict(type) {
    var self = this,
    map = this.mapInstance;

    if(this.boundary) {
      $.each(this.boundary, function(ii, vv) {
          map.data.remove(vv);
      })
    }

    if (type) {
        map.data.loadGeoJson(staticURL + 'map/js/' + type + '.json', {}, function(data) {
          map.data.setStyle({
              fillColor: '#C8C8C8',
              fillOpacity: .2,
              strokeColor: self.borderStroke,
              strokeOpacity: 1,
              strokeWeight: .5
          });
          self.boundary = data;
        });
    }
  },

  getStyles: function() {
    return [
      {
          "elementType": "geometry.fill",
          "stylers": [
              { "color": "#F8F4F0" },
              { "visibility": "on" },
              { "weight": 1 }
          ]
      },

      {
          "featureType": "administrative.country",
          "elementType": "geometry.stroke",
          "stylers": [
              { "color": this.borderStroke },
              { "visibility": "on" }
          ]
      },

      {
          "featureType": "administrative.country",
          "elementType": "labels.text.fill",
          "stylers": [
              { "color": "#3F3E3E" },
              { "visibility": "on" },
              { "weight": 1 }
          ]
      },

      {
          "featureType": "administrative.country",
          "elementType": "labels.text.stroke",
          "stylers": [
              { "color": "#3F3E3E" },
              { "visibility": "off" }
          ]
      },

      {
          "featureType": "water",
          "stylers": [
              { "visibility": "on" },
              { "color": "#BAD4ED" }
          ]
      },

      {
          "featureType": "road.highway",
          "stylers": [
              { "visibility": "on" },
              { "color": "#EAC485" },
              { "stroke": "#E7CE87" }
          ]
      }
    ];
  }
};


$(function() {
    MapPage.createMap(document.getElementById('map'), {
      center: {lat: 23, lng: 80},
      zoom: 4
    });
});
