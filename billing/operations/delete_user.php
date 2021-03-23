<?php
    include './connection.php';
    
    $billing = $_POST['billing'];
    $deleting_error = false;
    if(!$billing) {
        $deleting_error = true;
        include '../index.php';
        die();
    }

    $connection = connect_to_db();
    if (!$connection) {
        $connect_error = true;
        include '../results/results.php';
        die();
    } else {
        $query = "DELETE FROM `asterisk_users` WHERE account_id=? LIMIT 1";
        $stmt = mysqli_prepare($connection, $query);
        $stmt->bind_param('i', $billing);
        $stmt->execute();
        $success = true;
        if ($stmt->affected_rows == 0 && !$stmt->error) {
            $success = false;
            include '../results/results.php';
        } else {
            include '../results/results.php';
        }
        $stmt->close();
        die();
    }
