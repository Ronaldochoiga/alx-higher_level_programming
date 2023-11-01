#!/usr/bin/node
/**
  * fetches data and lists the title for all movies from https://swapi-api.hbtn.io/api/films/?format=json
  * you must use JQuery API for this particular task
  */
const $ = window.$;
const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, function (data) {
  const results = data.results;
  $.each(results, function (key, value) {
    $('UL#list_movies').append('<li>' + value.title + '</li>');
  });
});
