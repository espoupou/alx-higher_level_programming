#!/usr/bin/node
const $ = window.$;
$('DIV#red_header').click(function () {
  if ($('HEADER').hasClass('green')) {
    $('HEADER').removeClass('green');
    $('HEADER').addClass('red');
  } else {
    $('HEADER').removeClass('red');
    $('HEADER').addClass('green');
  }
});
