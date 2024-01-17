// Wait for the document to be ready
$(document).ready(function() {
  // Make an AJAX request using jQuery
  $.ajax({
    // Specify the URL to fetch data from
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    // Specify the request method (GET in this case)
    method: 'GET',
    // Define a success callback function
    success: function(response) {
      // Find the <div> with id hello using jQuery
      const helloDiv = $('DIV#hello');

      // Check if the <div> is found
      if (helloDiv.length > 0) {
        // Set the content of the <div> to the fetched translation
        helloDiv.text(response.hello);
      } else {
        // Log an error if the <div> is not found
        console.error('Hello div not found');
      }
    },
    // Define an error callback function
    error: function(error) {
      // Log the error if the request fails
      console.error('Error fetching translation:', error);
    }
  });
});