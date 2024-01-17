// Wait for the document to be ready
$(document).ready(function() {
  // Find the <div> with id red_header using jQuery
  const toggleHeaderDiv = $('#toggle_header');

  // Check if the <div> is found
  if (toggleHeaderDiv.length > 0) {
    // Attach a click event handler to the <div>
    toggleHeaderDiv.click(function() {
      // Find the <header> element using jQuery
      const headerElement = $('header');

      // Check if the <header> element is found
      if (headerElement.length > 0) {
        // Update the text color to red
        headerElement.toggleClass('red green')
      } else {
        // Log an error if the <header> element is not found
        console.error('Header element not found');
      }
    });
  } else {
    // Log an error if the <div> is not found
    console.error('Red header div not found');
  }
});