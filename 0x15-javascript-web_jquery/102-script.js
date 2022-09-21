document.addEventListener('DOMContentLoaded', () => {
  $('#btn_translate').click(function () {
    const url = 'https://stefanbohacek.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, function (data) {
      $('#hello').html(data.hello);
    });
  });
});
