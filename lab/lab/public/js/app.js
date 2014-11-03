/*global document, $, jQuery*/
function append_meetup(meetup) {
    var fields = ['city', 'state', 'country', 'link', 'lat', 'lon', 'members', 'name', 'who'];
    var $column_div = $('<div>');
    var $meetup_div = $('<div>');
    var $ul = $('<ul>');
    $column_div.addClass('col-sm-4');
    $meetup_div.addClass('well well-sm');
    $.each(fields, function() {
        var $li = $('<li>');
        $li.append($('<strong>').text(this + ': '));
        $li.append($('<span>').text(meetup[this]));
        $ul.append($li);
    });
    $meetup_div.append($ul);
    $column_div.append($meetup_div);
    $('#meetups').append($column_div);
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

