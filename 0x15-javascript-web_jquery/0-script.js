// Find the <header> element using document.querySelector
const headerElement = document.querySelector('header');

// Check if the <header> element is found
if (headerElement) {
  // Update the text color to red
  headerElement.style.color = '#FF0000';
} else {
  // Log an error if the <header> element is not found
  console.error('Header element not found');
}