/*!
 * Toggle search
 */
(function(){
	$('body').on('click', '[data-search-open], [data-search-close]', function(event) {
		event.preventDefault();
		if($(event.target).closest('[data-search-open]').size() > 0){
			$('body').addClass('is-search-active');
		} else {
			$('body').removeClass('is-search-active');
		}
	});
})();

/*!
 * Toggle nav
 */
(function(){
	$('body').on('click', '[data-nav-toggle]', function(event) {
		event.preventDefault();
		$('body').toggleClass('is-nav-active');
	}).on('click touchstart', '.top-a .nav', function(event) {
		if(event.target == this){
			event.preventDefault();
			$('body').removeClass('is-nav-active');
		}
	});
})();

/*!
 * Parallax
 */
(function(){
	if(typeof skrollr !== 'undefined'){
		$('.hero-b').each(function(index, el) {
			var $root = $(this);
			if(Modernizr.objectfit) $root.find('.bg-a img').attr({'data-0': 'transform: translate(0px,0px); opacity: 1;', 'data-400': 'transform: translate(0px,100px);opacity: 0;'});
			$root.find('.hx').attr({'data-0': 'transform: translate(0px,0px); opacity: 1;', 'data-300': 'transform: translate(0px,-50px);opacity: 0;'});
		});

		if(Modernizr.objectfit) $('.hero-c .bg-a img').attr({'data-0': 'transform: translate(0px,0px); opacity: 1;', 'data-500': 'transform: translate(0px,100px);opacity: 0.5;'});
		if(Modernizr.objectfit) $('.hero-a .bg-a img').attr({'data-0': 'transform: translate(0px,0px); opacity: 1;', 'data-700': 'transform: translate(0px,100px);opacity: 0.5;'});

		var s = skrollr.init({smoothScrolling: false});
		if(s.isMobile() || $('html').is('.touch')) s.destroy();
	};
})();

/*!
 * Multiply form fields
 */
(function(){
	$('body').on('click', '[data-cloner]', function(event) {
		event.preventDefault();
		var $cloner = $(this);
		var $parent = $cloner.closest('[data-clones]');
		var $origin = $parent.find('[data-origin]');
		$origin.clone().removeAttr('data-origin').insertAfter($origin);
	});
})();

/*!
 * Autosuggest select
 */
(function(){
	if(typeof $.fn.autoComplete != 'undefined'){
		$('.autosuggest[data-source]').each(function(index, el) {
			var $root = $(this);
			$root.autoComplete({
				minChars: $root.data('minchars') || 3,
				cache: true,
				source: function(term, response){
					try { xhr.abort(); } catch(e){}
					xhr = $.getJSON($root.data('source'), { q: term }, function(data){ response(data); });
				},
				onSelect: function(event, term, item){
					event.preventDefault();
				}
			});
		});
	}
})();

/*!
 * Tag input
 */
(function(){
	if(typeof $.fn.selectize != 'undefined'){
		$('[data-tags]').each(function(index, el) {
			var $root = $(this);
			var tags = $root.data('options')
			var options = [];
			if(typeof tags != 'undefined'){
				tags.split(/\s*,\s*/).forEach(function(element) {
					options.push({name: element})
				});
			};
			$root.selectize({
				valueField: 'name',
				labelField: 'name',
				searchField: 'name',
				options: options,
				persist: false,
				create: function(input) {
					return {
						name: input
					};
				}
			});
		});
	}
})();

/*!
 * Forms validation
 */
(function(){
	$('form.validate').each(function(formindex, el) {
		var $root = $(this);

		$root.find('[required]').each(function(fieldindex, el) {
			var $field = $(this);

			var $container = $field.closest('p, ul, ol');
			var classes = ['parsley-errors-wrapper', 'for-'+$field.attr('name')];
			$container.append('<span class="'+ classes.join(' ')+'" id="error-'+(formindex+1+ '-' + (fieldindex+1))+'"></span>');
			$field.attr('data-parsley-errors-container', '#error-'+(formindex+1 + '-' + (fieldindex+1)));
		});

		$root.parsley({
			errorsWrapper: '<span class="wrapper"></span>',
			errorTemplate: '<span class="error"></span>'
		}).on("field:error", function(fieldInstance){
			if (!$(fieldInstance.$element).is(':visible')) fieldInstance.validationResult = true;
		});
	});
})();

/*!
 * Signup forms
 */
(function(){
	$('.signup-b').on('submit', function(event) {
		//event.preventDefault();
		// ajax goes here
		//$(this).css('min-height', $(this).height()).toggleClass('is-sent');
	});
})();

/*!
 * Forms enhancements
 */
(function(){
	$('body').on('change.placeholder', 'select', function(e){
		$(this).toggleClass('placeholder', ($(this).val() == '' || $(this).val() == null));
	});

	var init = function(){
		$('select').trigger('change.placeholder');
		$('textarea.autoresize:not(.is-initialized)').each(function(index, el) {
			$(this).addClass('is-initialized').textareaAutoSize();
		});

		$('input[type=file]:not(.is-initialized)').each(function(index, el) {
			$(this).addClass('is-initialized').on('change', function(event) {
				$(this).toggleClass('filled', $(this).val() != '');
			});
		}).triggerHandler('change');
	};
	$(window).on('reinitialize.forms', init);
	init();
})();

/*!
 * Manage device/os/helpers classnames
 */
(function(){
	var ua = navigator.userAgent.toLowerCase();
	var standard = ['android', 'chrome', 'safari', 'samsungbrowser'];
	var classes = [];

	for (var i = 0, max = standard.length; i < max; i++) {
		if (ua.indexOf(standard[i]) != -1) {
			classes.push(standard[i]);
		}
	};

	if (ua.indexOf('android') > -1 && ua.indexOf('samsungbrowser') > -1) classes.push('native');
	if (ua.indexOf('android') > -1 && !(ua.indexOf('chrome') > -1) && !(ua.indexOf('firefox') > -1)) classes.push('native');
	if (ua.indexOf('crios') > -1) classes.push('chrome');
	if (ua.indexOf('iemobile') > -1) $('html').removeClass('no-touchevents').addClass('mie touchevents');
	if (ua.indexOf('iemobile/9.') > -1) classes.push('mie9');
	if (ua.indexOf('iemobile/10.') > -1) classes.push('mie10');
	if(/(ipad|iphone|ipod)/g.test(ua)) classes.push('ios');

	document.documentElement.className += ' ' + classes.join(' ');

	$(window).on('load', function(event) {
		$('.root-a').removeClass('is-loading');
	});
})();

/*!
 * Open external links in a new tab
 */
(function(){
	$('body').on('click', 'a[rel*="external"]', function(e){
		e.preventDefault();
		window.open($(this).attr('href'));
	});
})();

/*!
 * :last-child polyfill
 */
(function(){
	if(!document.addEventListener){
		[].forEach.call(document.querySelectorAll('*'), function(el){
			if (el.nextSibling === null) el.className += ' last-child';
		});
	}
})();

/*!
 * SVG fallback to PNG
 */
(function(){
	if ((typeof Modernizr != "undefined" && !Modernizr.svg) || document.querySelectorAll('html.android.native').length > 0) {
		var imgs = document.getElementsByTagName('img');
		var endsWithDotSvg = /.*\.svg$/
		for(var i = 0, l = imgs.length; i != l; ++i) {
			if(imgs[i].src.match(endsWithDotSvg)) {
				imgs[i].src = imgs[i].src.slice(0, -3) + 'png';
			}
		}
	}
})();