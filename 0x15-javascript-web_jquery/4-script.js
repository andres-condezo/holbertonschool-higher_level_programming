const redHeader = $('DIV#toggle_header');
const header = $('header');
$(redHeader).click(function () {
  header.toggleClass('red green');
});
