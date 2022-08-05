<?php
if (isset($_POST['sub'])) {
    $custemail = htmlspecialchars($_POST['custemail']);
    echo $custemail;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    <br />View Customer Flights
    <br />
    <form action="/viewCustomers" method="POST">
        <input type="text" name="custemail" placeholder="Customer to Search" required /></br>
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
    {% if recentdate %}
    <br />Most Frequent Customer
    <table>
        <th>Cust_email</th>
        <th>Name</th>
        <th>Building Number</th>
        <th>Street</th>
        <th>City</th>
        <th>State</th>
        <th>Phone Number</th>
        <th>Total of Tickets Bought</th>
        <tr>
            <td>{{input['cust_email']}}</td>
            <td>{{input['name']}}</td>
            <td>{{input['building_number']}}</td>
            <td>{{input['street']}}</td>
            <td>{{input['city']}}</td>
            <td>{{input['state']}}</td>
            <td>{{input['phone_number']}}</td>
            <td>{{recentdate}}</td>
        </tr>
    </table>
    {% endif %}

    {% if customerlist %}
    <br />{{custemail}} Flight History
    <table>
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
