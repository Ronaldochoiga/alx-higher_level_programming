#!/usr/bin/node
/**
  * Changes the color to red after clicking the DIV#red_header.
  * you must use the JQuery API
  */
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').addClass('red');
});
