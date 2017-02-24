(function($) {
	if ($("#messages .messages").length > 0)
	{
		$("#messages .messages li").each(function (i, el) {
			var content = $(this).html();
			$(".notification").append(content);
			
		});

		$(".notification").fadeIn('200', function() {
			setTimeout(function () {
				$(".notification").fadeOut();
			}, 2000);
		});
	}

	$("#community-search-form").on("submit", function(e) {
		var $form = $(this);
		var url = $form.attr("action");

		e.preventDefault();
		
		var address = $form.find("#f-city").val() + "%20" + $form.find("#f-state").val() + "%20" + $form.find("#f-zip").val();

		$.ajax({
			url: url,
			dataType: "json",
			data: { address: address },
			type: "GET",
			timeout: 20000,
			beforeSend: function () {
				$form.find(".button-a").hide();
				console.log("hide button");
			}
		})
		.always(function () {
			$form.find(".button-a").show();
			
		}).
		done(function (data) {
			console.log(data);
			// Attempt to parse the response data
			renderMap(data);
		});
	});

	renderMap();

	function renderMap(coordinates) {
		if ($(".mapbox #map").length < 1)
			return;
		var mapOptions = {
     		center: new google.maps.LatLng(41.850033, -87.6500523),
     		zoom: 4,
     		zoomControl: true,
     		zoomControlOptions: {
     			position: google.maps.ControlPosition.RIGHT_CENTER
     		},
     		mapTypeControl: true,
     		mapTypeControlOptions: {
     			style: google.maps.MapTypeControlStyle.DROPDOWN_MENU
     		},
     		streetViewControl: false,
     		scaleControl: false,
     		panControl: false
     	};
     	var map = new google.maps.Map(document.getElementById("map"), mapOptions);
     	var infoWindow = new google.maps.InfoWindow();

     	if (typeof coordinates == "object") {
     		var m = coordinates;
     		var place = new google.maps.LatLng(m.latitude, m.longitude);
     		var marker = new google.maps.Marker({
     			title: m.name,
     			map: map,
     			position: place,
     			icon: m.image,
     			content: '<a target="_blank" href="' + m.website + '">' + m.content + '</a>'
     		});
     		google.maps.event.addListener(marker, "click", function() {
     			infoWindow.setContent(this.content);
     			infoWindow.open(map, this);
     		});
     	}

	}

})(jQuery);