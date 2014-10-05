<%inherit file="/auth_base.mako" />

<h1>Login</h1>
<form role="form" name="login" method="post" action="/login">
  <div class="form-group">
    <label for="email">Email Address</label>
    <input type="email" class="form-control" id="email" placeholder="test@example.com" />
  </div>
  <div class="form-group">
    <label for="password">Password</label>
    <input type="password" class="form-control" id="password"  placeholder="Password" />
  </div>
  <button type="submit" class="btn btn-primary">Login</button>
</form>
