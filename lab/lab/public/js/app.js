/*global document, $, jQuery*/
function display_user(user) {
    var $user_div = $('#user');
    var $avatar = $user_div.find('.avatar');
    var $name = $user_div.find('.name');
    var $username = $user_div.find('.username');
    var $email = $user_div.find('.email');
    var $loc = $user_div.find('.location');
    var $company = $user_div.find('.company');
    var $blog = $user_div.find('.blog');
    if (user.avatar_url) {
        $avatar.attr('src', user.avatar_url);
    }
    if (user.name) {
        $name.text(user.name);
    }
    if (user.username) {
        $username.text(user.username);
    }
    if (user.email) {
        $email.text(user.email);
    }
    if (user.location) {
        $loc.text(user.location);
    }
    if (user.company) {
        $company.text(user.company);
    }
    if (user.blog) {
        $blog.text(user.blog);
    }
}

function fetch_user(id) {
    var url = '/github/user/' + id;
    $.getJSON(url)
        .success(function(data) {
            if (data.message === 'Not Found') {
                console.log('User not found.');
            } else {
                display_user(data);
            }
        })
        .fail(function() {
            console.log('Failed to retrieve user.');
        });
}

$(document).ready(function() {
    $('#user_search_button').click(function() {
        fetch_user($('#user_search_input').val());
    });
});
