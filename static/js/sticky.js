window.onscroll = function() {myFunction()};

// Get the header
var header = document.getElementById("header-row");

// Get the offset position of the navbar
var sticky = header.offsetTop;

// Add the sticky class to the header when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}
// https://www.w3schools.com/howto/howto_js_sticky_header.asp