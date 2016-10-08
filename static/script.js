var markers = [];
var paths = [];
var pathDistances = [];
var markerInfo = [];
var direction_url = document.getElementById('direction').innerHTML;
var weather_url = document.getElementById('weather').innerHTML;
var search_url = document.getElementById('search').innerHTML;
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -7.3632438, lng: 110.5155871},
    zoom: 8
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

  // get weather information
  $.ajax({
    type: "GET",
    url: weather_url,
    data: {
      lat: position.lat,
      lng: position.lng,
    },
    success: function(data) {
      markerInfo.push(data);

      updateInfo();
      // $('#result').text(JSON.stringify(data));
    }
  });

  addRoute(lastMarker, marker, map, direction_url);
}

function clearMarkers() {
  for(var key in markers) {
    markers[key].setMap(null);
  }
  markers = [];
  markerInfo = [];
}

function clearPaths() {
  for(var key in paths) {
    paths[key].setMap(null);
  }
  paths = [];
  pathDistances = [];
}

function clearAll() {
  clearMarkers();
  clearPaths();
  updateDistance();
  updateInfo();
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
        path: google.maps.geometry.encoding.decodePath(data.points),
        geodesic: true,
        strokeColor: "#FF0000",
        strokeOpacity: 1.0,
        strokeWeight: 2
      });

      newPath.setMap(map);
      paths.push(newPath);
      pathDistances.push(data.distance.value);

      updateDistance();
      // $('#result').text(JSON.stringify(data));
    }
  });
}

function updateDistance() {
  var result = 0;
  for(var key in pathDistances) {
    result += pathDistances[key];
  }

  document.getElementById('distance-label').innerHTML = result;
}

function getWeather() {

}

function updateInfo() {
  var result = '';
  if(markerInfo.length > 0) {
    for(var key in markerInfo) {
      result += '<tr>';
      var info = markerInfo[key];
      result += '<td>'+info.coord.lat+', '+info.coord.lon+'</td>';
      result += '<td>'+info.main.temp+' C</td>';
      result += '<td>'+info.main.humidity+'%</td>';
      result += '<td>'+info.weather[0].main+'</td>';
      result += '<td>'+info.wind.speed+' m/s</td>';
      result += '<td>'+info.wind.deg+'</td>';
      result += '</tr>';
    }
  }
  document.getElementById('point-info-tbody').innerHTML = result;
}

function searchLocation(location) {
  clearAll();
  
  $.ajax({
    type: "GET",
    url: search_url,
    data: {
      location: location
    },
    success: function(data) {
      if(data) {
        var point = new google.maps.LatLng(data.lat, data.lng);
        map.panTo(point);
      }
      // $('#result').text(JSON.stringify(data));
    }
  });
}
