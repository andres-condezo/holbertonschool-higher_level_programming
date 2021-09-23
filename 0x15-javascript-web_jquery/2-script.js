const redHeader = $('DIV#red_header');
const header = $('header');
$(redHeader).click(function () {
  header.css('color', '#FF0000');
});
