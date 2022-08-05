<?php
if (isset($_POST['sub'])) {
    $status = htmlspecialchars($_POST['status']);
    echo $status;
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
    Count Number of Flights with Inputted Status
    <form action="/flightstatusCount" method="POST">
        <input type="text" name="status" placeholder="Status" required /> </br>
        <input type="submit" name ="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
        {% endif %}
    </form>
    <br />
    {% if Input %}
    Number of Flights That Are {{Input['flight_status']}}: {{Input['Total']}}
    {% endif %}
    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
