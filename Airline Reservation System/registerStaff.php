<?php
if (isset($_POST['sub'])) {
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);
    $airline = htmlspecialchars($_POST['airline']);
    $email = htmlspecialchars($_POST['email']);
    echo $username;
    echo $password;
    echo $airline;
    echo $email;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <form action="/registerAuthStaff" method="POST">
        <input type="text" name="username" placeholder="Username" required /><br>
            <input type="password" name="password" placeholder="Password" required />
        </br>
        <input type="text" name="airline" placeholder="Airline Employer" required /><br>
            <input type="email" name="email" placeholder="Email" required />
        </br>

        <input type="submit" name="sub"value=Register />
        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
    </form>
    <a href="/">Go back</a>
</body>
</html>
