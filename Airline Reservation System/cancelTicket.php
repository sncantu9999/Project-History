<?php
if (isset($_POST['sub'])) {
    $airline = htmlspecialchars($_POST['airline']);
    $flightnumber = htmlspecialchars($_POST['flightnumber']);
    echo $airline;
    echo $flightnumber;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    {% if error %}
    <p class="error"><strong>Error:</strong> {{error}}</p>
    {% endif %}
    {% if noinput %}
    <br />Cancel Ticket
    <br />
    <form action="/cancelmyTicket" method="POST">
        <input type="text" name="airline" placeholder="Airline Name" required /></br>
        <input type="text" name="flightnumber" placeholder="Flight Number" required /></br>
        <input type="submit" name ="sub" value=Search />
    </form>
    {% endif %}
    {% if input %}
    Ticket Cancelled!
    {% endif %}
    <a href="/home">Go back</a>


</body>


</html>
