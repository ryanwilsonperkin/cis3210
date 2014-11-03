function get_meetups(text) {
    url = '/meetup/groups/' + text;
    return $.getJSON(url, function(data) {
        $.each(data, function(index, meetup) {
            // Add meetup to page.
        });
    });
}
