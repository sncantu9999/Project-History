<?php
if (isset($_POST['sub'])) {
    $username = htmlspecialchars($_POST['username']);
	$password = htmlspecialchars($_POST['password']);
    $airline = htmlspecialchars($_POST['airline']);
    echo $username;
    echo $password;
    echo $airline;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <form action="/loginAuthStaff" method="POST">
        <input type="text" name="username" placeholder="username" required /><br>
            <input type="password" name="password" placeholder="password" required />
        </br>
        <input type="text" name="airline" placeholder="airline employer" required /><br />
        <input type="submit" name="sub" value=Login />
        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
    </form>

    <a href="/">Go back</a>

</body>


</html>