/*
stolen from https://codepen.io/voronianski/pen/aicwk
*/

function typeWriter(text, n) {
  if (n < (text.length)) {
    $('.hi').html(text.substring(0, n+1));
    n++;
    setTimeout(function() {
      typeWriter(text, n)
    }, 60);
  }
}

var text = $('.hi').data('text');

typeWriter(text, 0);