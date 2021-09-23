const url = 'https://www.fourtonfish.com/hellosalut/';

function fetchHello () {
	const lang = $('INPUT#language_code').val();
	const fullUrl = ${url}?lang=${lang};

	$.get(fulUrl, function (data) {
		$('DIV#hello').text(data.hello);
	});
}

$(document).ready(() => {
	$('INPUT#language_code').keydown((e) => {
		if (e.keyCode === 13) { fetchHello(); }
	});

	$('INPUT#btn_translate').on({
		click: fetchHello
	});
});
