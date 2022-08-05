<?php
if (isset($_POST['sub'])) {
    $flightNumber = htmlspecialchars($_POST['flightNumber']);
    $departuredatetime = htmlspecialchars($_POST['departuredatetime']);
    $departureAirport = htmlspecialchars($_POST['departureAirport']);
    $arrivalAirport = htmlspecialchars($_POST['arrivalAirport']);
    $arrivaldatetime = htmlspecialchars($_POST['arrivaldatetime']);
    $airplaneid = htmlspecialchars($_POST['airplaneid']);
    $baseprice = htmlspecialchars($_POST['baseprice']);
    $status = htmlspecialchars($_POST['status']);
    $departdate = htmlspecialchars($_POST['departdate']);
    $returndate = htmlspecialchars($_POST['returndate']);
    echo $flightNumber;
    echo $departuredatetime;
    echo $departureAirport;
    echo $arrivalAirport;
    echo $arrivaldatetime;
    echo $airplaneid;
    echo $baseprice;
    echo $status;
    echo $departdate;
    echo $returndate;
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
    Flight was Created!
    {% endif %}

    {% if not success %}
    <br />Show Airline Flights
    <br />Option 1: If You Submit All Fields Blank, It Will Show the Airline Flights Taking Place Over the Next 30 Days
    <br />Option 2: Fill in Fields to Create a New Flight
    <br />Starting and Ending Ranges in (YYYY-MM-DD HH:MM:SS) (HH in Military Time)
    <br />
    <form action="/createnewFlight" method="POST">
        <input type="text" name="flightNumber" placeholder="Flight Number"/></br>
        <input type="text" name="departuredatetime" placeholder="Departure Date/Time" /></br>
        <input type="text" name="departureAirport" placeholder="Departure Airport" /></br>
        <input type="text" name="arrivalAirport" placeholder="Arrival Airport" /> </br>
        <input type="text" name="arrivaldatetime" placeholder="Arrival Date/Time" /></br>
        <input type="text" name="airplaneid" placeholder="Airplane ID" /></br>
        <input type="text" name="baseprice" placeholder="Base Price" /></br>
        <input type="text" name="status" placeholder="Flight Status" /> </br>
        <input type="text" name="departdate" placeholder="Departure Date" /></br>
        <input type="text" name="returndate" placeholder="Return Date" /> </br>

        <input type="submit" name ="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>
    {% endif %}
    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>
    {% if input %}
    <br />Flights Found
    <table>
        <th>Airline Name</th>
        <th>Flight Number</th>
        <th>Departure Date/Time</th>
        <th>Departure Airport</th>
        <th>Arrival Airport</th>
        <th>Flight Status</th>

        {% for line in input %}
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
    <a href="/homeforStaff">Go back</a>
</body>


</html>
