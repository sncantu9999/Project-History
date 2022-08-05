<?php
if (isset($_POST['sub'])) {
    $airline = htmlspecialchars($_POST['airline']);
    $flightNumber = htmlspecialchars($_POST['flightNumber']);
    $departureDate = htmlspecialchars($_POST['departureDate']);
    echo $airline;
    echo $flightNumber;
    echo $departureDate;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <br />Search Flight Status
    <br />Departure Date in format (YYYY/MM/DD)
    <form action="/NologinsearchFlightStatus" method="POST">
        <input type="text" name="airline" placeholder="Airline Name" required /><br>
            <input type="text" name="flightNumber" placeholder="Flight Number" required /><br />
        <input type="text" name="departureDate" placeholder="Departure Date" required /><br />
        <input type="submit" name = "sub" value=Search />

        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
    </form>

    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>
    <br />
    {% if status %}
    <table>
        <th>Flight Status</th>
        <tr>
            <td>{{status['flight_status']}}</td>
        </tr>
    </table>
    {% endif %}
    <br />
    <a href="/">Go back</a>

</body>


</html>