/*global document, $, jQuery*/

function render_user(data) {
    var $user = $('<div>');
    $user.attr('id', 'user');

    if (data.avatar_url) {
        var $avatar = $('<img>');
        $avatar.addClass('img-responsive');
        $avatar.attr('src', data.avatar_url);
        $user.append($avatar);
    }

    if (data.name) {
        var $name = $('<h1>');
        $name.text(data.name);
        $user.append($name);
    }

    if (data.username) {
        var $username = $('<p>');
        $username.text(data.username);
        $user.append($username);
    }

    if (data.email) {
        var $email = $('<p>');
        $email.text(data.email);
        $user.append($email);
    }

    if (data.location) {
        var $location = $('<p>');
        $location.text(data.location);
        $user.append($location);
    }

    if (data.company) {
        var $company = $('<p>');
        $company.text(data.company);
        $user.append($company);
    }

    if (data.blog) {
        var $blog = $('<p>');
        $blog.text(data.blog);
        $user.append($blog);
    }
    return $user;
}

function fetch_user(id) {
    var url = '/github/user/' + id;
    $.getJSON(url)
        .success(function(data) {
            if (data.message === 'Not Found') {
                console.log('User not found.');
            } else {
                $('#user_section .container').append(render_user(data));
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
