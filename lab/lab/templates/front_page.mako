<!DOCTYPE html>
<html lang="en">
<head>
  <title>CIS3210 Lab 3</title>
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <link href='http://fonts.googleapis.com/css?family=Droid+Serif:400,700' rel='stylesheet' type='text/css'>
  <link rel="stylesheet" type="text/css" href="/css/bootstrap.min.css" media="screen" />
  <link rel="stylesheet" type="text/css" href="/css/main.css" />
</head>
<body>
  <nav class="navbar navbar-default navbar-fixed-top" role="navigation">
    <div class="container-fluid">
      <div class="navbar-header">
        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar-collapse">
          <span class="sr-only">Toggle navigation</span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="#">The Gateless Gate</a>
      </div>
      <div class="collapse navbar-collapse" id="navbar-collapse">
        <ul class="nav navbar-nav navbar-right">
          % if c.user:
            <li><p class="navbar-right navbar-text"><span class="glyphicon glyphicon-user"></span>
              Logged in as ${c.user.first_name | h} ${c.user.last_name | h}</p></li>
            <li><a href="/logout">Logout</a></li>
          % else:
            <li><a href="/login">Login</a></li>
            <li><a href="/register">Register</a></li>
          % endif
        </ul>
      </div>
    </div>
  </nav>
  <header id="intro">
    <div class="container">
      <div class="cta">
        <h1>The Gateless Gate</h1>
        <p class="lead">Study the Zen koans and become enlightened.</p>
      </div>
    </div>
    <span class="glyphicon glyphicon-chevron-down"></span>
  </header>
  <section>
    <div class="container">

      <hr />
      <div id="descriptionRow" class="row">
        <div class="col-sm-8 col-sm-offset-2">
          <p id="description" class="lead">Here you will find a collection of 48 Zen koans, compiled by master Mumon Ekai. Koans are a form of literary riddle, used to test your understanding of Zen philosophy.</p>
        </div>
      </div>
      <hr />

      <div id="koanSelectorRow" class="row">
        <div class="col-xs-8 col-xs-offset-2">
          <form role="form" id="koanForm" class="form-inline">
            <div class="form-group">
              <label for="koanSelector">Koan Selector</label>
              <select id="koanSelector" class="form-control"></select>
            </div>
            <button id="fetchRandomKoan" class="btn btn-success" type="button">Random koan</button>
          </form>
        </div>
      </div>

      <div id="koanRow" class="row">
        <div class="col-sm-8 col-sm-offset-2">
          <div id="koan"></div>
        </div>
      </div>

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
  <script type="text/javascript" src="/js/app.js"></script>
</body>
</html>
