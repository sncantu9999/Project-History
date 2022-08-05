<?php
if (isset($_POST['sub'])) {
    $airportname = htmlspecialchars($_POST['airportname']);
    $city = htmlspecialchars($_POST['city']);
    $country = htmlspecialchars($_POST['country']);
    $type = htmlspecialchars($_POST['type']);
    echo $airportname;
    echo $city;
    echo $country;
    echo $type;
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
    Airport was Added!
    {% endif %}

    {% if not success %}
    <br />Add Airport to Registry
    <br />
    <form action="/addAirport" method="POST">
        <input type="text" name="airportname" placeholder="Airport Name" required /><br>
            <input type="text" name="city" placeholder="City" required />
        </br>
        <input type="text" name="country" placeholder="Country" required /><br>
            <input type="text" name="type" placeholder="Type (domestic, international, or domestic/international)" required />
        </br>
        <br />
        <input type="submit" name ="sub"value=Search />
        {% if error %}
        <p class="error">
            <strong>Error:</strong> {{error}}
        </p>
        {% endif %}
    </form>

    {% endif %}

    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
