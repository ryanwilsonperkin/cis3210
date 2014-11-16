<!DOCTYPE html>
<html lang="en">
<head>
  <title>GitHub Resume</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css" media="screen" />
  <link href="css/ripples.min.css" rel="stylesheet">
  <link href="css/material-wfont.min.css" rel="stylesheet">
  <link rel="stylesheet" type="text/css" href="/css/main.css" />
</head>
<body>
  <header id="intro_section">
    <div class="container">
      <h1>GitHub Resume</h1>
      <p class="lead">Use your GitHub as your own personal resume.</p>
    </div>
  </header>
  <section id="seach_section">
    <div class="container">
      <div class="row">
        <div class="col-md-6 col-md-offset-3">
          <form action="javascript:void(0);">
            <div class="form-group">
              <label for="user_search_input">Search for a user.</label>
              <input type="text" class="form-control" id="user_search_input">
            </div>
            <button type="submit" class="btn btn-primary" id="user_search_button">Search</button>
          </form>
        </div>
      </div>
    </div>
  </section>
  <section id="user_section">
    <div class="container">
      <div class="errors"></div>
    </div>
  </section>
  <section id="repo_section">
    <div class="container">
      <div class="errors"></div>
    </div>
  </section>
  <footer>
    <div class="container">
      <hr />
      <p>Developed by Ryan Wilson-Perkin (0719644)</p>
    </div>
  </footer>
  <script type="text/javascript" src="/js/jquery.js"></script>
  <script type="text/javascript" src="/js/bootstrap.min.js"></script>
  <script src="js/ripples.min.js"></script>
  <script src="js/material.min.js"></script>
  <script type="text/javascript" src="/js/app.js"></script>
</body>
</html>
