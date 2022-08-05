<?php
if (isset($_POST['sub'])) {
    $departureAirport = htmlspecialchars($_POST['departureAirport']);
    $arrivalAirport = htmlspecialchars($_POST['arrivalAirport']);
    $departureDate = htmlspecialchars($_POST['departureDate']);
    $returnDate = htmlspecialchars($_POST['returnDate']);
    echo $departureAirport;
    echo $arrivalAirport;
    echo $departureDate;
    echo $returnDate;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    Search Upcoming Flights
    <br />Departure Date and Return Date in format (YYYY/MM/DD)
    <form action="/NologinsearchFlights" method="POST">
        <input type="text" name="departureAirport" placeholder="Departure Airport" required /><br>
            <input type="text" name="arrivalAirport" placeholder="Arrival Airport" required />
        </br>
        <input type="text" name="departureDate" placeholder="Departure Date" required /><br>
            <input type="text" name="returnDate" placeholder="Return Date" />
        </br>
        <input type="submit" name ="sub"value=Search />
        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
    </form>
    <br />
    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>
    {% if posts %}
    <table>
        <th>Airline Name</th>
        <th>Flight Number</th>
        <th>Departure Date/Time</th>
        <th>Departure Airport</th>
        <th>Arrival Airport</th>

        {% for line in posts %}
        <tr>
            <td>{{line['airline_name']}}</td>
            <td>{{line['flight_number']}}</td>
            <td>{{line['departure_date_time']}}</td>
            <td>{{line['departure_airport']}}</td>
            <td>{{line['arrival_airport']}}</td>
        </tr>
        {% endfor %}
        {% endif %}
    </table>
    <a href="/">Go back</a>
</body>


</html>
