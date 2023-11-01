#!/usr/bin/node
/**
  * Updates the <header> element text to New Heade!!! when the user clicks on DIV#update_header
  * you must use JQuery API for this task
  */
const $ = window.$;
$('DIV#update_header').click(function () {
  $('header').text('New Header!!!');
});
