$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, item) {
    $('#list_movies').append('<li>' + item.title + '</li>');
  });
});
