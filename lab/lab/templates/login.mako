<%inherit file="/auth_base.mako" />

<h1>Login</h1>
<form role="form" name="login" method="post" action="/login">
  % if len(c.form_errors):
    <div class="alert alert-danger" role="alert">
      <button type="button" class="close" data-dismiss="alert">
        <span aria-hidden="true">&times;</span><span class="sr-only">Close</span>
      </button>
    % for error in c.form_errors:
      <strong>${error}</strong>
    % endfor
    </div>
  % endif
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
