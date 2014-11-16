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

function render_repo(data) {
    var $repo = $('<div>');
    $repo.attr('class', 'repo');

    var $name = $('<h1>');
    $name.text(data.name);
    $repo.append($name);

    var $language = $('<p>');
    $language.text(data.language);
    $repo.append($language);

    var $html_url = $('<p>');
    $html_url.text(data.html_url);
    $repo.append($html_url);

    if (data.description) {
        var $description = $('<p>');
        $description.text(data.description);
        $repo.append($description);
    }
    return $repo;
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

function fetch_repos(id) {
    var url = '/github/repos/' + id;
    $.getJSON(url)
        .success(function(data) {
            if (data.message === 'Not Found') {
                console.log('Repos not found.');
            } else {
                $.each(data, function(index, repo_data) {
                    $('#repo_section .container').append(render_repo(repo_data));
                });
            }
        })
        .fail(function() {
            console.log('Failed to retrieve user.');
        });
}

$(document).ready(function() {
    $('#user_search_button').click(function() {
        var id = $('#user_search_input').val();
        fetch_user(id);
        fetch_repos(id);
    });
});
