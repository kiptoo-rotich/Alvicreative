$(document).ready(function() {
    $("#history").hide()
    $("#who_we_are").mouseover(function() {
        $("#history").show()
        $("#who_we_are,.centered").hide()
    });

    $("#who_we_are").mouseout(function() {
        $("#history").hide()
        $("#who_we_are,.centered").show()
    });
});


var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("navbar").style.top = "0";
    } else {
        document.getElementById("navbar").style.top = "-70px";
    }
    prevScrollpos = currentScrollPos;
}


// First hide them all
$("#fades div").hide();

function fades($div, cb) {
    $div.fadeIn(100, function() {
        $div.fadeOut(100, function() {
            var $next = $div.next();
            if ($next.length > 0) {
                fades($next, cb);
            } else {
                // The last element has faded away, call the callback
                cb();
            }
        });
    });
}

function startFading($firstDiv) {
    fades($firstDiv, function() {
        startFading($firstDiv);
    });
}

startFading($("#fades div:first-child"));