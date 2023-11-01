#!/usr/bin/node
/**
  * Updates color to red on clicking the div#read_header
  * you must use the JQuery API
  */
const $ = window.$;
$('DIV#red_header').click(function () {
  $('header').css('color', 'red');
});
