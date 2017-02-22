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
		e.preventDefault();
	});
	
})(jQuery);