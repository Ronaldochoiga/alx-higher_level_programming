#!/usr/bin/node
/**
  * Changes the header elemnt color to red
  *
  * only JQuery api allowed
  */
const $ = window.$;
$(document).ready(function () {
  $('header').css('color', 'red');
});
