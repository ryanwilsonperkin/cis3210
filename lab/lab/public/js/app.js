$(function() {
    $.getJSON('/koans', function(koansList) {
        $.each(koansList, function(index, value) {
            $('#koanSelector').append($('<option></option>').text(value));
        });
    });
});
