<%inherit file="/auth_base.mako" />

<h1>Register</h1>
<form role="form" name="register" method="post" action="/register">
  <div class="form-group">
    <label for="firstName">First Name</label>
    <input type="text" class="form-control" id="firstName" placeholder="First Name" />
  </div>
  <div class="form-group">
    <label for="lastName">Last Name</label>
    <input type="text" class="form-control" id="lastName" placeholder="Last Name" />
  </div>
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
