// Wait for the document to be ready
$(document).ready(function() {
  // Find the <div> with id add_item using jQuery
  const addDiv = $('#add_item');

  // Check if the <div> is found
  if (addDiv.length > 0) {
    // Attach a click event handler to the <div>
    addDiv.click(function() {
      // create an li element using jQuery
      const listChild = "<li>Item</li>";

      // append the element to the list
      $("UL.my_list").append(listChild)
    });
  } else {
    // Log an error if the <div> is not found
    console.error('Add item div not found');
  }
});