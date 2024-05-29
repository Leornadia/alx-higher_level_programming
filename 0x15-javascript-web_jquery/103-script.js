$(document).ready(function() {
  function translateHello() {
    const languageCode = $('#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/${languageCode}`;

    $.get(apiUrl, function(data) {
      $('#hello').text(data.hello);
    })
    .fail(function() {
      $('#hello').text('Translation not available');
    });
  }

  $('#btn_translate').click(translateHello);

  $('#language_code').on('keypress', function(event) {
    if (event.which === 13) {
      translateHello();
    }
  });
});
