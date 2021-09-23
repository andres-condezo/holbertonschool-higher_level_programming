const redHeader = $('DIV#red_header');
const header = $('header');
$(redHeader).click(function () {
  header.addClass('red');
});
