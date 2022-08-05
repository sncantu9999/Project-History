<?php
if (isset($_POST['sub'])) {
    $newemail = htmlspecialchars($_POST['newemail']);
    echo $newemail;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    {% if not Input %}
    <form action="/addEmail" method="POST">
        <input type="email" name="newemail" placeholder="New Email" required /><br />
        <input type="submit" name ="sub"value=Submit />
        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
        {% endif %}
        {% if Input %}
        Email was Added!
        {% endif %}
    </form>
    <a href="/homeforStaff">Go back</a>
</body>
</html>
