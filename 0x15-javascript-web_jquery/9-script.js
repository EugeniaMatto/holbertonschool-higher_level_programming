$( document ).ready(function() {
  $.get("https://fourtonfish.com/hellosalut/?lang=fr", function(r) {
    $('#hello').text(r.hello);
  });
});
