#!/usr/bin/node
const $ = window.$;
$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, textStatus) {
  $('DIV#hello').text(data.hello);
});
