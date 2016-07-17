$(function() {
    $("select[name=lang]").on("change", function() {
        var $this = $(this);
        var search = window.location.search.slice(1).split("&");
        var ss = [];
        for (var ii=0; ii < search.length; ii++) {
            if (search[ii].length > 0 && search[ii].search(/lang\=/gi) < 0) {
                ss.push(search[ii]);
            }
        }
        if ($this.val()) {
            ss.push("lang=" + $this.val());
        }
        window.location = window.location.pathname + "?" + ss.join("&");
    });
});
