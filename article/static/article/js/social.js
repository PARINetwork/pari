$(function(){
    if (('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch) {
	// Mobile device.
	$(".hidden.whatsapp").removeClass("hidden")
    }
});
