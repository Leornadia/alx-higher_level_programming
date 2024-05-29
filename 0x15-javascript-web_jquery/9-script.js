$(document).ready(function() {
    // Fetch the translation of "hello" in French
    $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data) {
        // Display the translation in the <div> with id="hello"
        $('#hello').text(data.hello);
    });
});

