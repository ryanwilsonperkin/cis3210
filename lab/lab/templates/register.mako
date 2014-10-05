<%inherit file="/auth_base.mako" />

<h1>Register</h1>
<p class="lead">or <a href="/login">login</a></p>
<hr />
<form role="form" name="register" method="post" action="/register">
  % if len(c.form_errors):
    <div class="alert alert-danger" role="alert">
      <button type="button" class="close" data-dismiss="alert">
        <span aria-hidden="true">&times;</span><span class="sr-only">Close</span>
      </button>
      <ul>
      % for error in c.form_errors:
        <li><strong>${error}</strong></li>
      % endfor
      </ul>
    </div>
  % endif
  <div class="form-group">
    <label for="firstName">First Name</label>
    <input type="text" class="form-control" id="firstName" name="firstName" placeholder="First Name" />
  </div>
  <div class="form-group">
    <label for="lastName">Last Name</label>
    <input type="text" class="form-control" id="lastName" name="lastName" placeholder="Last Name" />
  </div>
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" class="form-control" id="email" name="email" placeholder="test@example.com" />
  </div>
  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" class="form-control" id="password" name="password" placeholder="Password" />
  </div>
  <button type="submit" class="btn btn-primary">Login</button>
</form>
