<?php
if (isset($_POST['sub'])) {
    $flightNumber = htmlspecialchars($_POST['flightNumber']);
    $departuredate = htmlspecialchars($_POST['departuredate']);
    $departureAirport = htmlspecialchars($_POST['departureAirport']);
    $arrivalAirport = htmlspecialchars($_POST['arrivalAirport']);
    $newstatus = htmlspecialchars($_POST['newstatus']);
    echo $flightNumber;
    echo $departuredate;
    echo $departureAirport;
    echo $arrivalAirport;
    echo $newstatus;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    {% if success %}
    Status Was Updated!
    {% endif %}
    {% if not success %}
    <br />Change Flight Status
    <br />
    <form action="/changeflightstatus" method="POST">
        <input type="text" name="flightNumber" placeholder="Flight Number" required /></br>
        <input type="text" name="departuredate" placeholder="Departure Date" required /></br>
        <input type="text" name="departureAirport" placeholder="Departure Airport" required /></br>
        <input type="text" name="arrivalAirport" placeholder="Arrival Airport" required /> </br>
        <input type="text" name="newstatus" placeholder="New Flight Status" required /> </br>
        <br />
        <input type="submit" name ="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>
    {% endif %}

    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
