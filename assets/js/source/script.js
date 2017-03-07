(function($) {

	window.USI = {
		init: function () {
			this.initNotifications();
			this.initCommunityMapSearch();
			this.initAppSearch();
		},
		// Display flash notifications
		initNotifications: function () {
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
		},
		// Initialize community map search widget on homepage
		initCommunityMapSearch: function () {
			var self = this;
			$("#community-search-form").on("submit", function(e) {
				var $form = $(this);
				var url = $form.attr("action");

				e.preventDefault();
				
				var address = "";

				if ($.trim($form.find("#f-city").val()) !== "")
					address = address + $form.find("#f-city").val() + ",";


				if ($.trim($form.find("#f-state").val()) !== "")
					address = address + $form.find("#f-state").val() + ",";

				if ($.trim($form.find("#f-zip").val()) !== "")
					address = address + $form.find("#f-zip").val();


				$.ajax({
					url: url,
					dataType: "json",
					data: { address: address },
					type: "GET",
					timeout: 20000,
					beforeSend: function () {
						$form.find(".button-a").hide();
						$form.find(".loading").show();
					}
				})
				.fail(function () {
					self.renderMap([]);
				})
				.always(function () {
					$form.find(".button-a").show();
					$form.find(".loading").hide();
					
				}).
				done(function (data) {
					self.renderMap(data);
				});
			});

			if ($("#community-list").length < 1)
			{
				self.renderMap();
			}
			else
			{
				var communities = new Array();
				$("#community-list li").each(function(i, el) {

					var community = {};
					community.latitude = $(el).data("lat");
					community.longitude = $(el).data("lon");
					community.name = $(el).data("name");
					community.content = $(el).data("name");
					community.website = $(el).data("website");

					communities.push(community);
				});
				self.renderMap(communities);
			}

			
		},
		// Display Google map
		renderMap: function (coordinates) {
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

	     	// If coordinate data is one community/object
	     	if (coordinates.constructor === Object) {
	     		this.createGoogleMapMarker(coordinates, map, infoWindow);
	     		
	     	}
	     	// If coordinate data is a list communities/objects
	     	else if(coordinates.constructor === Array)
	     	{
	     		for (var i = 0; i< coordinates.length; i++)
	     		{
	     			this.createGoogleMapMarker(coordinates[i], map, infoWindow);
	     		}
	     	}

		},
		// Add marker on Google map
		createGoogleMapMarker: function(coordinate, map, infoWindow) {
			var m = coordinate;
			var place = new google.maps.LatLng(m.latitude, m.longitude);

			var content;
			if (m.website == "")
				content = m.content;
			else
				content = '<a target="_blank" href="' + m.website + '">' + m.content + '</a>'

     		var marker = new google.maps.Marker({
     			title: m.name,
     			map: map,
     			position: place,
     			content: content
     		});

     		google.maps.event.addListener(marker, "click", function() {
     			infoWindow.setContent(this.content);
     			infoWindow.open(map, this);
     		});
		},
		initAppSearch: function () {
			if ($('#app-search-form').length < 1)
				return;

			var q = $.query.get('q');
			var sector = $.query.get('sector');
			var order = $.query.get('order');
			
			if (typeof q == "string")
				$('#app-search-form').find("[name='q']").val(q);
			if (typeof sector == "string")
				$('#app-search-form').find("[name='sector']").val(sector).removeClass("placeholder");
			if ($.trim(order) != "")
			{

				$('#app-search-form').find("[name='order']").val(order);
			}
			else
			{
				$('#app-search-form').find("[name='order']").val("desc");
			}

		}
	}

	window.USI.init();
})(jQuery);