$(document).ready(function() {
    function supports_audio() {
        var a = document.createElement('audio');
        return !!(a.canPlayType);
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

