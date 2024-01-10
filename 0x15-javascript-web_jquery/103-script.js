const $ = window.$;
window.onload = function () {
  $('INPUT#btn_translate').click(function () {
    const lan = $('INPUT#language_code').val();
    $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      const lan = $('INPUT#language_code').val();
      $.get('https://fourtonfish.com/hellosalut/?lang=' + lan, function (data, textStatus) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
};
