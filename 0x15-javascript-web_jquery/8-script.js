// Wait for the document to be ready
$(document).ready(function() {
  // Make an AJAX request using jQuery
  $.ajax({
    // Specify the URL to fetch data from
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    // Specify the request method (GET in this case)
    method: 'GET',
    // Define a success callback function
    success: function(response) {
      // Find the <ul> with id list_movies using jQuery
      const moviesList = $('#list_movies');

      // Check if the <ul> is found
      if (moviesList.length > 0) {
        // Loop through each movie in the response and append a list item to the <ul>
        response.results.forEach(function(movie) {
          moviesList.append(`<li>${movie.title}</li>`);
        });
      } else {
        // Log an error if the <ul> is not found
        console.error('Movies list not found');
      }
    },
    // Define an error callback function
    error: function(error) {
      // Log the error if the request fails
      console.error('Error fetching movies:', error);
    }
  });
});