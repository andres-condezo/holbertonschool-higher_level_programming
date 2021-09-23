const red_header = $('DIV#toggle_header');
const header = $('header');
$(red_header).click(function () {
  header.toggleClass('red green');
});
