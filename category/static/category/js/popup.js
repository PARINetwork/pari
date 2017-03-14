$(function () {
    $('.preview').on('click', function (event) {
        event.preventDefault();
        $('.pop-up').magnificPopup('open');
    });

    $('.pop-up').magnificPopup({
		delegate: 'a',
		type: 'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
        image: {
			tError: '<a href="%url%">The image #%curr%</a> could not be loaded.',
        }
	});
});
