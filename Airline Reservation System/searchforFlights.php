<?php
if (isset($_POST['sub'])) {
    $departureAirport = htmlspecialchars($_POST['departureAirport']);
    $arrivalAirport = htmlspecialchars($_POST['arrivalAirport']);
    $from = htmlspecialchars($_POST['from']);
    $to = htmlspecialchars($_POST['to']);
    echo $departureAirport;
    echo $arrivalAirport;
    echo $from;
    echo $to;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <br />Search For Upcoming Flights
    <br />Departure and Return Dates in (YYYY-MM-DD)
    <br />
    <form action="/searchFlightsforCust" method="POST">
        <input type="text" name="departureAirport" placeholder="Departure Airport" required /></br>
        <input type="text" name="arrivalAirport" placeholder="Arrival Airport" required /></br>
        <input type="text" name="from" placeholder="Departure Date" required /></br>
        <input type="text" name="to" placeholder="Return Date (round trips)" /> </br>
        <input type="submit" name="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>

    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>
    {% if Input %}
    <br />Flights Found
    <table>
        <th>Airline Name</th>
        <th>Flight Number</th>
        <th>Departure Date/Time</th>
        <th>Departure Airport</th>
        <th>Arrival Airport</th>
        <th>Flight Status</th>
        {% for line in Input %}
        <tr>
            <td>{{line['airline_name']}}</td>
            <td>{{line['flight_number']}}</td>
            <td>{{line['departure_date_time']}}</td>
            <td>{{line['departure_airport']}}</td>
            <td>{{line['arrival_airport']}}</td>
            <td>{{line['flight_status']}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
    <br />
    Purchase Flight
    <form action="/purchaseflight" method="POST">
        <input type="text" name="airline" placeholder="Airline Name" required /></br>
        <input type="text" name="flightnumber" placeholder="Flight Number" required /></br>
        <input type="text" name="cardnum" placeholder="Card Number" required /> </br>
        <input type="text" name="cardname" placeholder="Card Name" required /></br>
        <input type="text" name="expdate" placeholder="Expiration Date" required /></br>
        <input type="text" name="cardtype" placeholder="Card Type (debit or credit)" required /></br>
        <input type="submit" value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>
    <a href="/home">Go back</a>

</body>


</html>
