<?php
if (isset($_POST['sub'])) {
    $flightNumber = htmlspecialchars($_POST['flightNumber']);
    $newprice = htmlspecialchars($_POST['newprice']);
    echo $flightNumber;
    echo $newprice;
}
?>
<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta charset="utf-8" />
    <title></title>
</head>
<body>
    {% if error %}
    <p class="error">
        <strong>Error:</strong> {{error}}
    </p>
    {% endif %}
    {% if input %}
    <br />Change Base Price
    <br />
    <form action="/changebaseprice" method="POST">
        <input type="text" name="flightNumber" placeholder="Flight Number" required/></br>
        <input type="text" name="newprice" placeholder="New Price" required/></br>
        <input type="submit" name ="sub" value=Search />
    </form>
    {% endif %}

    {% if success %}
    Price Updated!
    {% endif %}

    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
