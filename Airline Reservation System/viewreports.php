<?php
if (isset($_POST['sub'])) {
    $start = htmlspecialchars($_POST['start']);
    $to = htmlspecialchars($_POST['to']);
    echo $start;
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
    <br />Total Number of Tickets Sold
    <br />Starting and Ending Ranges in (YYYY-MM-DD)
    <br />
    <form action="/viewReports" method="POST">
        <input type="text" name="start" placeholder="Starting Range" required /></br>
        <input type="text" name="to" placeholder="Ending Range" required /> </br>
        <input type="submit" name="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>
    {% if input %}
    <br />Total Number of Tickets Sold Over Range: {{input['Total']}}
    {% endif %}
    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>
    {% if input2 %}
    <br />Month Wise Ticket Breakdown
    <table>
        <th>Month</th>
        <th>Year</th>
        <th>Tickets Sold</th>
        {% for i,j in input2.items() %}
        {% for k,v in j.items() %}
        <tr>
            <td>{{k}}</td>
            <td>{{i}}</td>
            <td>{{v}}</td>
        </tr>
        {% endfor %}
        {% endfor %}
    </table>
    {% endif %}
    <br />
    <a href="/homeforStaff">Go back</a>
</body>


</html>
