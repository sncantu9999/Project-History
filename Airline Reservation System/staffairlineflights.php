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
    <br />Show Airline Flights
    <br />Option 1: If You Submit All Fields Blank, It Will Show the Airline Flights Taking Place Over the Next 30 Days
    <br />Option 2: Fill in Fields to See Custom Results
    <br />Starting and Ending Ranges in (YYYY-MM-DD)
    <br />
    <form action="/staffairlineFlights" method="POST">
        <input type="text" name="departureAirport" placeholder="Departure Airport" /></br>
        <input type="text" name="arrivalAirport" placeholder="Arrival Airport" /></br>
        <input type="text" name="from" placeholder="Starting Range" /></br>
        <input type="text" name="to" placeholder="Ending Range" /> </br>
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

    {% if customerlist %}
    <br />Customers
    <table>
        <th>Customer Email</th>
        <th>Ticket ID</th>
        <th>Airline Name</th>
        <th>Flight Number</th>
        <th>Departure Date/Time</th>
        <th>Phone Number</th>
        <th>Name</th>
        <th>Sold Price</th>
        <th>Purchase Date/Time</th>

        {% for line in customerlist %}
        <tr>
            <td>{{line['cust_email']}}</td>
            <td>{{line['ticket_id']}}</td>
            <td>{{line['airline_name']}}</td>
            <td>{{line['flight_number']}}</td>
            <td>{{line['departure_date_time']}}</td>
            <td>{{line['phone_number']}}</td>
            <td>{{line['name']}}</td>
            <td>{{line['sold_price']}}</td>
            <td>{{line['purchase_date_time']}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}
    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
