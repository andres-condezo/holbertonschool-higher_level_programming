$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  data.results.forEach((el) => {
    $('#list_movies').append('<li>' + el.title + '</li>');
  });
});
