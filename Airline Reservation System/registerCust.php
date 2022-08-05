<?php
if (isset($_POST['sub'])) {
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);
    echo $username;
    echo $password;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
	<meta charset="utf-8" />
	<title></title>
</head>
<body>
	<form action="/registerAuthCust" method="POST">
		<input type="email" name="username" placeholder="email" required /> </br>
		<input type="password" name="password" placeholder="password" required /></br>
		<input type="submit" name="sub"value=Register />
		{% if error %}
		<p class="error"><strong>Error:</strong> {{error}}</p>
		{% endif %}
	</form>
	<a href="/">Go back</a>
</body>
</html>
