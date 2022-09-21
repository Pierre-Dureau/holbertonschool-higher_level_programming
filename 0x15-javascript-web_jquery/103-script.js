document.addEventListener('DOMContentLoaded', () => {
  $('#btn_translate').click(function () {
    const url = 'https://stefanbohacek.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, function (data) {
      $('#hello').html(data.hello);
    });
  });
  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      const url = 'https://stefanbohacek.com/hellosalut/?lang=' + $('#language_code').val();
      $.get(url, function (data) {
        $('#hello').html(data.hello);
      });
    }
  });
});
