// Wait for the document to be ready
$(document).ready(function() {
  // Make an AJAX request using jQuery
  $.ajax({
    // Specify the URL to fetch data from
    url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
    // Specify the request method (GET in this case)
    method: 'GET',
    // Define a success callback function
    success: function(response) {
      // Find the <div> with id character using jQuery
      const characterDiv = $('#character');

      // Check if the <div> is found
      if (characterDiv.length > 0) {
        // Display the character name in the <div>
        characterDiv.text(response.name);
      } else {
        // Log an error if the <div> is not found
        console.error('Character div not found');
      }
    },
    // Define an error callback function
    error: function(error) {
      // Log the error if the request fails
      console.error('Error fetching character:', error);
    }
  });
});