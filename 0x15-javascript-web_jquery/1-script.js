//Include jQuery library (you can use a CDN or download it locally)
// Wait for the document to be ready
$(document).ready(function() {
  // Find the <header> element using jQuery
  const headerElement = $('header');

  // Check if the <header> element is found
  if (headerElement.length > 0) {
    // Update the text color to red
    headerElement.css('color', '#FF0000');
  } else {
    // Log an error if the <header> element is not found
    console.error('Header element not found');
  }
});