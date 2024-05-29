$(document).ready(function() {
    // Fetch movie data from the given URL
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
        // Loop through each movie and append its title to the <ul> with id="list_movies"
        data.results.forEach(function(movie) {
            $('#list_movies').append('<li>' + movie.title + '</li>');
        });
    });
});

