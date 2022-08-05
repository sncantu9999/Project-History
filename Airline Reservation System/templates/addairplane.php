<?php
if (isset($_POST['sub'])) {
    $idnum = htmlspecialchars($_POST['idnum']);
    $numseats = htmlspecialchars($_POST['numseats']);
    $comp = htmlspecialchars($_POST['comp']);
    $age = htmlspecialchars($_POST['age']);
    echo $idnum;
    echo $numseats;
    echo $comp;
    echo $age    ;
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
    Airplane was Added!
    {% endif %}

    {% if not success %}
    <br />Add Airplane to Registry
    <br />
    <form action="/addAirplane" method="POST">
        <input type="text" name="idnum" placeholder="Airplane ID Number" required /><br>
            <input type="text" name="numseats" placeholder="Number of Seats" required />
        </br>
        <input type="text" name="comp" placeholder="Manufactoring Company" required /><br>
            <input type="text" name="age" placeholder="Age" required />
        </br>
        <br />
        <input type="submit" name ="sub" value=Search />
        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
    </form>

    {% endif %}
    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>
    <br />

    {% if input %}
    <br />Airplanes Registered
    <table>
        <th>Airline Name</th>
        <th>ID Number</th>
        <th>Number of Seats</th>
        <th>Manufactoring Company</th>
        <th>Age</th>

        {% for line in input %}
        <tr>
            <td>{{line['airline_name']}}</td>
            <td>{{line['id_num']}}</td>
            <td>{{line['num_seats']}}</td>
            <td>{{line['manufactoring_company']}}</td>
            <td>{{line['age']}}</td>
        </tr>
        {% endfor %}
    </table>
    {% endif %}

    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
