var markers = [];
var paths = [];
var direction_url = document.getElementById('direction').innerHTML;
function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -7.3632438, lng: 110.5155871},
    zoom: 15
  });

  google.maps.event.addListener(map, 'click', function(event) {
    placeMarker(event.latLng, map);
  });
}

function placeMarker(position, map) {
  var marker = new google.maps.Marker({
    position: position,
    map: map
  });

  var lastMarker = markers.slice(-1).pop();
  markers.push(marker);
  // map.panTo(position);

  addRoute(lastMarker, marker, map, direction_url);
}

function clearMarkers() {
  for(var key in markers) {
    markers[key].setMap(null);
  }
  markers = [];
}

function clearPaths() {
  for(var key in paths) {
    paths[key].setMap(null);
  }
  paths = [];
}

function clearAll() {
  clearMarkers();
  clearPaths();
}

function addRoute(markerBegin, markerEnd, map, url) {
  if(null == markerBegin || null == markerEnd) return;
  var begin = markerBegin.position.lat()+','+markerBegin.position.lng();
  var end = markerEnd.position.lat()+','+markerEnd.position.lng();

  $.ajax({
    type: "GET",
    url: url,
    data: {
      begin: begin,
      end: end,
    },
    success: function(data) {
      var newPath = new google.maps.Polyline({
        path: google.maps.geometry.encoding.decodePath(data),
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2
      });

      newPath.setMap(map);
      paths.push(newPath);
      // $('#result').text(JSON.stringify(data));
    }
  });
}
