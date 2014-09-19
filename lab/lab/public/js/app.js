var g_koansList;

// Fetch koan from server and insert it on the page.
function fetchKoan(id) {
    koanDiv = $('#koan');
    $.getJSON('/koans/' + id, function(koan) {
        // Clear away old koan.
        koanDiv.hide();
        koanDiv.empty();

        // Insert new koan title.
        koanDiv.append($('<h2></h2>').text(koan.title));

        // Insert new koan text.
        $.each(koan.text, function(index, val) {
            koanDiv.append($('<p></p>').text(val));
        });

        // Fade in new koan.
        koanDiv.fadeIn();
    });
};

$(document).ready(function() {
    // Populate koansList.
    $.getJSON('/koans', function(koansList) {
        g_koansList = koansList;
        $.each(koansList, function(index, val) {
            $('#koanSelector').append($('<option></option>').text(val));
        });
    });

    // Add functionality to fetchKoan.
    $('#fetchKoan').click(function(e) {
        // Get index of koan from value of koanSelector.
        index = g_koansList.indexOf($('#koanSelector').val());
        fetchKoan(index);
    });

    // Add functionality to fetchRandomKoan.
    $('#fetchRandomKoan').click(function(e) {
        // Get random index within range.
        index = Math.floor(Math.random() * g_koansList.length);
        // Set koanSelector to reflect randomly chosen index.
        $('#koanSelector option').eq(index).prop('selected', true)
        fetchKoan(index);
    });

    // Initially display the first koan.
    fetchKoan(0);
});
