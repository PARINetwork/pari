
$(function () {
    var lastScrollTop = 0;
    window.addEventListener('scroll', function (e) {
        var st = window.pageYOffset || document.documentElement.scrollTop;
        var ele = document.getElementById("article-read-time");
        var content_container_outerHeight = $(".content-container").outerHeight();
        if (st > lastScrollTop ) {
            if (content_container_outerHeight != st){
                ele.style.visibility = "visible";
            }
            if (content_container_outerHeight <= st){
                ele.style.visibility = "hidden";
            }
            var header = document.getElementById("header")
            header.style.visibility = "hidden"
            $(header).css("transition-duration","300ms")
            var search_panel = document.getElementById("main_search_panel");
            $(search_panel).css("transition-duration","300ms")
            search_panel.style.visibility = "hidden";

        } else {
            ele.style.visibility = "hidden";
            var header = document.getElementById("header");
            header.style.visibility = "visible"
            $(header).css("transition-duration","300ms")
            var search_panel = document.getElementById("main_search_panel");
            $(search_panel).css("transition-duration","300ms")
            search_panel.style.visibility = "visible"

        }
        lastScrollTop = st;
    }, false);
})