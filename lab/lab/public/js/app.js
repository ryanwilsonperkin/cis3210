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

function arrowFadeLoop() {
    $('header .glyphicon').animate({opacity: 0.25}, {duration: 1000})
                          .animate({opacity: 1.0}, {duration: 1000, complete: arrowFadeLoop});
}

$(document).ready(function() {
    // Populate koansList.
    var g_koansList;
    $.getJSON('/koans', function(koansList) {
        g_koansList = koansList;
        $.each(koansList, function(index, val) {
            $('#koanSelector').append($('<option></option>').text(val));
        });
    });

    // Add functionality to fetchKoan.
    $('#koanSelector').change(function() {
        // Get index of koan from value of koanSelector.
        index = g_koansList.indexOf($(this).val());
        fetchKoan(index);
    });

    // Add functionality to fetchRandomKoan.
    $('#fetchRandomKoan').click(function(e) {
        // Get random index within range.
        index = Math.floor(Math.random() * g_koansList.length);
        // Set koanSelector to reflect randomly chosen index.
        $('#koanSelector option').eq(index).prop('selected', true).trigger('change');
    });

    // Add scroll event to down arrow.
    $('header .glyphicon').click(function() {
        $('html, body').animate({
            scrollTop: $("#descriptionRow").offset().top
        }, 500);
    });

    // Trigger arrow fade in/out loop.
    arrowFadeLoop();

    // Initially display the first koan.
    fetchKoan(0);
});
