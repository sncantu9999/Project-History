<?php
if (isset($_POST['sub'])) {
    $airline = htmlspecialchars($_POST['airline']);
    $flightnumber = htmlspecialchars($_POST['flightnumber']);
    $departureAirport = htmlspecialchars($_POST['departureAirport']);
    $arrivalAirport = htmlspecialchars($_POST['arrivalAirport']);
    $rating = htmlspecialchars($_POST['rating']);
    $comment = htmlspecialchars($_POST['comment']);
    echo $airline;
    echo $flightnumber;
    echo $departureAirport;
    echo $arrivalAirport;
    echo $rating;
    echo $comment;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    {% if noinput %}
    <br />Rate/Comment Past Flight
    <br />
    <form action="/ratecommentFlight" method="POST">
        <input type="text" name="airline" placeholder="Airline Name" required /></br>
        <input type="text" name="flightnumber" placeholder="Flight Number" required /></br>
        <input type="text" name="departureAirport" placeholder="Departure Airport" required /></br>
        <input type="text" name="arrivalAirport" placeholder="Arrival Airport" required /></br>
        <input type="text" name="rating" placeholder="Rating (0 - 10)" required /></br>
        <input type="text" name="comment" placeholder="Comment" required /></br>
        <input type="submit" name="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>
    {% endif %}
    {% if input %}
    Review Submitted!
    {% endif %}
    <a href="/home">Go back</a>


</body>


</html>
