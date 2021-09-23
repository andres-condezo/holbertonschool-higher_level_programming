const url = 'https://www.fourtonfish.com/hellosalut/';

$(document).ready(() => {
  $('INPUT#BTN_TRANSLATE').on({
    click: () => {
      const lang = $('INPUT#language_code').val();
      const fullUrl = `${url}?lang=${lang}`;

      $.get(fullUrl, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
