<?php
if (isset($_POST['sub'])) {
    $newnumber = htmlspecialchars($_POST['newnumber']);
    echo $newnumber;
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
    <form action="/addNumber" method="POST">
        <input type="text" name="newnumber" placeholder="Add Phone Number" required /> </br>
        <input type="submit" name ="sub"value=Submit />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
        {% endif %}
        {% if Input %}
        Phone Number was Added!
        {% endif %}
    </form>
    <a href="/homeforStaff">Go back</a>
</body>
</html>
