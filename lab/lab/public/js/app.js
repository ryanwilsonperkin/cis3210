/*global document, $, jQuery*/
function github_user(id) {
    var url = '/github/user/' + id;
    $.getJSON(url)
        .success(function(data) {
            $('#user_name').text(data.name);
        })
        .fail(function() {
            $('#user_name').text('Error');
        });
}

$(document).ready(function() {
    $('#user_search_button').click(function() {
        github_user($('#user_search_input').val());
    });
});
