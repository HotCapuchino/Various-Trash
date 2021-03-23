<?php
    include './connection.php';

    $updating_error_fields = [];
    foreach ($_POST as $key => $value) {
        if (!$value) {
            $updating_error_fields[$key] = true;
        }
    }
    if (sizeof($adding_error_fields) !== 0) {
        include '../index.php';
        die();
    }

    $billing = $_POST['billing'];
    $phone = $_POST['phone'];
    $balance = $_POST['balance'];

    $connection = connect_to_db();
    if (!$connection) {
        $connect_error = true;
        include '../results/results.php';
        die();
    } else {
        $query = "UPDATE `asterisk_users` SET phone=?, balance=? WHERE account_id=? LIMIT 1";
        $stmt = mysqli_prepare($connection, $query);
        $stmt->bind_param('sii', $phone, $balance, $billing);
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
