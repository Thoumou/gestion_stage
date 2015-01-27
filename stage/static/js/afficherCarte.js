$(document).ready(function(){
	var latitude = $('.lat').html();
	latitude = parseFloat(latitude.replace(',', '.'));
	
	var longitude = $('.lon').html();
	longitude = parseFloat(longitude.replace(',', '.'));

	var carte;
	var initialize;
	var latLngEntreprise = new google.maps.LatLng(latitude, longitude);
	var latLngPerso;
	var markerPerso;
	var markerEntreprise;
	
	function geolocationSuccess(position) {
		latLngPerso = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
		directionsDisplay = new google.maps.DirectionsRenderer();
		

		
		var myOptions = {
			zoom : 14,
			center : latLngEntreprise,
			mapTypeId : google.maps.MapTypeId.ROADMAP
		};

		// Draw the map
		carte = new google.maps.Map(document.getElementById("carte"), myOptions);
		directionsDisplay.setMap(carte)

		// Place the marker
		markerPerso = new google.maps.Marker({
			map: carte,
			position: latLngPerso,
			title:"Vous etes ici"
		});
		
		markerEntreprise = new google.maps.Marker({
			map: carte,
			position: latLngEntreprise,
			title:"L'entreprise"
		});
	}
	
	function calcRoute() {
		var directionsService = new google.maps.DirectionsService();
		var request = {
			origin:latLngPerso,
			destination:latLngEntreprise,
			travelMode: google.maps.TravelMode.DRIVING
		};
		directionsService.route(request, function(response, status) {
			if (status == google.maps.DirectionsStatus.OK) {
				directionsDisplay.setDirections(response);
			}
		});
		console.log
		markerPerso.setMap(null);
		markerEntreprise.setMap(null);
		
	}

	function geolocationError(positionError) {
		document.getElementById("error").innerHTML += "Error: " + positionError.message + "<br />";
	}
 
	function geolocateUser() {
		// If the browser supports the Geolocation API
		if (navigator.geolocation){
			var positionOptions = {
				enableHighAccuracy: true,
				timeout: 10 * 1000 // 10 seconds
			};
			navigator.geolocation.getCurrentPosition(geolocationSuccess, geolocationError, positionOptions);
		}
		else{
			document.getElementById("error").innerHTML += "Your browser doesn't support the Geolocation API";
		}
	}
	
	geolocateUser();
	
	$("#itineraire").click(function(e) {
		e.preventDefault();
		calcRoute();
	});
	
});