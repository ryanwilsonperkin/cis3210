/*global document, $, jQuery*/
function append_meetup(meetup) {
    var fields = ['city', 'link', 'lat', 'lon', 'members', 'name', 'who'];
    var $ul = $('<ul>');
    $.each(fields, function() {
        var $li = $('<li>');
        $li.append($('<strong>').text(this + ': '));
        $li.append($('<span>').text(meetup[this]));
        $ul.append($li);
    });
    $('#meetups').append($ul);
}

function get_meetups(text) {
    var url = '/meetup/groups/' + text;
    $.getJSON(url)
        .success(function(data) {
            $('#meetups').empty();
            $.each(data, function() {
                append_meetup(this);
            });
        })
        .fail(function() {
            var $error = $('<div>');
            $error.addClass('alert alert-warning');
            $error.attr('role', 'alert');
            $error.text('error: Could not fetch data from api.meetup.com');
            $('#meetups').append($error);
        });
}

$(document).ready(function() {
    // Bind get_meetups functionality to form.
    $('#topic_search_button').click(function() {
        get_meetups($('#topic_search_input').val());
    });
});

