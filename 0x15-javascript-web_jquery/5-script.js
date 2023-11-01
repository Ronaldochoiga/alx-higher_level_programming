#!/usr/bin/node
/**
  * adds a <li> element to a ul.list when the user clicks on the tag DIV#add_item
  * use JQuery only for this particalr task
  */
const $ = window.$;
$('DIV#add_item').click(function () {
  $('UL.my_list').append('<li
