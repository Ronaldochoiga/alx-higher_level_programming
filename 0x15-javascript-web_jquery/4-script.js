#!/usr/bin/node
/**
  * when the user click on DIV#toggle_header, the class must be updated to green ;
  * and the reverse when the button is red
  * use JQUERY only
  */
const $ = window.$;
$('DIV#toggle_header').click(function () {
  $('header').toggleClass('green');
  $('header').toggleClass('red');
});
