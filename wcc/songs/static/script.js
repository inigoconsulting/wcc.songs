$(document).ready(function() {
    function supports_audio() {
        var a = document.createElement('audio');
        if (!!(a.canPlayType)) {
            return a.canPlayType('audio/mpeg');
        } else {
            return false   
        };
    }
    if (supports_audio()) {
        $('.audioSupported').show();
        $('.audioNotSupported').hide();
    }
    else {
        $('.audioSupported').hide();
        $('.audioNotSupported').show();
    }
})

