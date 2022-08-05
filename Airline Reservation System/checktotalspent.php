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
    <br />Check Total Spent
    <br />Starting and Ending Range in (YYYY-MM-DD)
    <br />Option 1: If Left Blank, Total Spent Over Last Year and a Past 6 Month Breakdown is Shown
    <br />Option 2: If All Fields are Filled In, a Breakdown Between Those Dates is Shown
    <form action="/checkTotalSpent" method="POST">
        <input type="text" name="start" placeholder="Starting Range" /></br>
        <input type="text" name="to" placeholder="Ending Range" /></br>
        <input type="submit" name ="sub"value=Search />
        {% if error %}
        <p class="error"><strong>Error:</strong> {{error}}</p>
        {% endif %}
    </form>

    {% if firstinput %}
    <br /> Total Spent Over Past Year: {{firstinput['Total']}}
    <br />
    <br />
    {% endif %}

    {% if fifthinput %}
    <br /> Total Spent Over Range: {{fifthinput['Total']}}
    <br />
    <br />
    {% endif %}

    <style type="text/css">
        table, th, td {
            border: 1px solid black;
        }
    </style>

    {% if secondinput %}
    <br />  6 Month Breakdown
    {% endif %}

    {% if thirdinput %}
    <br /> Range Breakdown
    {% endif %}

    {% if fourthinput %}
    <table>
        <th>Month</th>
        <th>Year</th>
        <th>Total</th>
        {% for i,j in fourthinput.items() %}
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
    <a href="/home">Go back</a>
</body>


</html>
