<?php
if (isset($_POST['sub'])) {
    $airline = htmlspecialchars($_POST['airline']);
    $departureAirport = htmlspecialchars($_POST['departureAirport']);
    $arrivalAirport = htmlspecialchars($_POST['arrivalAirport']);
    $from = htmlspecialchars($_POST['from']);
    $to = htmlspecialchars($_POST['to']);
    echo $airline;
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
    <br />Search My Flights
    <br />Starting Date and Ending Date in (YYYY-MM-DD)
    <br />
    <br />Option 1: If You Submit All Fields Blank, All of Your Future Flights Will Appear
    <br />Option 2: Please Fill in All Fields to See Custom Results
    <form action="/determinemyFlights" method="POST">
        <input type="text" name="airline" placeholder="Airline Name" /> </br>
        <input type="text" name="departureAirport" placeholder="Departure Airport" /></br>
        <input type="text" name="arrivalAirport" placeholder="Arrival Airport" /></br>
        <input type="text" name="from" placeholder="Starting Date" /> </br>
        <input type="text" name="to" placeholder="Ending Date" /> </br>
        <input type="submit" name ="sub"value=Search />
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
        <th>Purchase Price</th>
        <th>Flight Status</th>
        {% for line in Input %}
        <tr>
            <td>{{line['airline_name']}}</td>
            <td>{{line['flight_number']}}</td>
            <td>{{line['departure_date_time']}}</td>
            <td>{{line['departure_airport']}}</td>
            <td>{{line['arrival_airport']}}</td>
            <td>{{line['sold_price']}}</td>
            <td>{{line['flight_status']}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    <a href="/home">Go back</a>

</body>


</html>
