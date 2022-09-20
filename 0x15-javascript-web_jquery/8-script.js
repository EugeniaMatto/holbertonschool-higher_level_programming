$(function() {
  $.get("https://swapi-api.hbtn.io/api/films/?format=json", function(r) {
    for (let i in r.results) {
      $('UL#list_movies').append('<li>' + r.results[i].title + '</li>');
    }
  });
});
