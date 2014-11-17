/*global document, $, jQuery*/

function language_icon(language) {
    var language_icon_map = {
        'C': 'icon-c',
        'Clojure': 'icon-clojure',
        'C++': 'icon-cplusplus',
        'C#': 'icon-csharp',
        'CSS': 'icon-css',
        'HTML': 'icon-html',
        'Java': 'icon-java',
        'JavaScript': 'icon-javascript',
        'Objective-C': 'icon-objc',
        'Perl': 'icon-perl',
        'PHP': 'icon-php',
        'Python': 'icon-python',
        'Ruby': 'icon-ruby',
        'Scala': 'icon-scala',
        'Shell': 'icon-shell',
    };
    var icon = language_icon_map[language];
    if (icon) {
        return $('<i>', {'class': 'language-icon ' + icon});
    }
    return '';
}

function render_user(data) {
    var $user = $('<div>', {
        'class': 'well',
    });
    var $row = $('<div>', {
        'class': 'row',
    });
    var $col_left = $('<div>', {
        'class': 'col-sm-3',
    });
    var $col_right = $('<div>', {
        'class': 'col-sm-9',
    });
    var $avatar = $('<img>', {
        'class': 'avatar img-responsive',
        'src': data.avatar_url,
    });
    var $name = $('<h1>', {
        'text': data.name,
    });
    var $login = $('<small>', {
        'text': data.login,
    });
    var $email = $('<p>', {
        'text': data.email,
    });
    var $location = $('<p>', {
        'text': data.location,
    });
    var $company = $('<p>', {
        'text': data.company,
    });
    var $blog = $('<p>', {
        'text': data.blog,
    });

    // Construct left column.
    $col_left.append($avatar);

    // Construct right column.
    var $login_link = $('<a>', {
        'href': data.html_url,
    }).append($login);
    $name.append($('<br>'));
    $name.append($login_link);
    $col_right.append($name);
    if (data.email) {
        var $email_link = $('<a>', {
            'href': 'mailto:' + data.email,
        }).append($email);
        $email.prepend($('<i>', {'class': 'mdi-communication-email'}));
        $col_right.append($email_link);
    }
    if (data.blog) {
        var $blog_link = $('<a>', {
            'href': data.blog,
        }).append($blog);
        $blog.prepend($('<i>', {'class': 'mdi-action-explore'}));
        $col_right.append($blog_link);
    }
    if (data.company) {
        $company.prepend($('<i>', {'class': 'mdi-communication-business'}));
        $col_right.append($company);
    }
    if (data.location) {
        $location.prepend($('<i>', {'class': 'mdi-communication-location-on'}));
        $col_right.append($location);
    }

    $row.append($col_left);
    $row.append($col_right);
    $user.append($row);
    return $user;
}

function render_repo(data) {
    var $repo = $('<div>', {
        'class': 'repo well',
    });
    var $name = $('<h1>', {
        'text': data.name,
    });
    var $name_link = $('<a>', {
        'href': data.html_url,
    }).append($name);
    var $language = $('<p>', {
        'text': 'Programmed in ' + (data.language || 'an unrecognized language'),
    });
    var $stargazers = $('<p>', {
        'text': data.stargazers_count,
    });
    var $forks = $('<p>', {
        'text': data.forks_count,
    });
    var $description = $('<p>', {
        'class': 'lead',
        'text': data.description,
    });

    $language.prepend(language_icon(data.language));
    $stargazers.prepend($('<strong>', {'text': 'Stars: '}));
    $stargazers.prepend($('<i>', {'class': 'mdi-action-grade'}));
    $forks.prepend($('<strong>', {'text': 'Forks: '}));
    $forks.prepend($('<i>', {'class': 'mdi-communication-call-split'}));

    $repo.append($name_link);
    if (data.description) {
        $repo.append($description);
    }
    $repo.append($language);
    $repo.append($stargazers);
    $repo.append($forks);
    return $repo;
}

// Sort by descending star count.
function sort_repos(repos) {
    repos.sort(function (a,b) {
        return b.stargazers_count - a.stargazers_count;
    });
}

function fetch_user(id) {
    var url = '/github/user/' + id;
    $.getJSON(url)
        .success(function(data) {
            if (data.message === 'Not Found') {
                console.log('User not found.');
            } else {
                $('#user').empty();
                $('#user').append(render_user(data));
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
                sort_repos(data);
                $('#repos').empty();
                $.each(data, function(index, repo_data) {
                    $('#repos').append(render_repo(repo_data));
                });
            }
        })
        .fail(function() {
            console.log('Failed to retrieve user.');
        });
}

$(document).ready(function() {
    $.material.init();
    $('#user_search_button').click(function() {
        var id = $('#user_search_input').val();
        fetch_user(id);
        fetch_repos(id);
    });
});
