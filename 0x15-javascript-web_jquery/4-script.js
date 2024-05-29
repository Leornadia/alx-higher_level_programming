$(document).ready(function() {
    // Add a click event handler to the <div> with id="toggle_header"
    $('#toggle_header').click(function() {
        // Check if the <header> element has the class 'red'
        if ($('header').hasClass('red')) {
            // If it has the class 'red', remove 'red' and add 'green'
            $('header').removeClass('red').addClass('green');
        } else {
            // If it doesn't have the class 'red', remove 'green' and add 'red'
            $('header').removeClass('green').addClass('red');
        }
    });
});

