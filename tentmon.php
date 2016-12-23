<?php

$dbhost = "localhost";
$dbuser = "tentweb";
$dbpass = "JC96vm5LxRQRcF9Q";
$dbname = "growsys";

$OUTPUT = "<div id=\"tentmon\">\r\n";

// create mysql connection
$myconn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);

if ($myconn->connect_error){

    die("Connection Failed: " . $myconn->connect_error);
}

$sqlCurrent = "SELECT r_time, ROUND((temp*1.8+32), 2) AS temp, ROUND(humidity, 2) AS humidity FROM growsys.tent_env WHERE r_time BETWEEN DATE_SUB(NOW(), INTERVAL 1 MINUTE) AND NOW()";

$resultCurrent = $myconn->query($sqlCurrent);

if ($resultCurrent->num_rows > 0) {

    while($row = $resultCurrent->fetch_assoc()) {
        $OUTPUT .= "<span class=\"valCurr\"> Temperature: " . $row["temp"] . " F </span><br/>\r\n";
        $OUTPUT .= "<span class=\"valCurr\">Humidity: " . $row["humidity"] . " % </span><br/>\r\n";
    }
}


$OUTPUT .= "</div>";

?>

<!DOCTYPE html>
<html>
<head>
<title> Tent Montior </title>

</head>
<body>

<div id="display">

<?php echo($OUTPUT); ?>

</div>
</body>
</html>