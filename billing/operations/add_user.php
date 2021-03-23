<?php 
    include './connection.php';

    $adding_error_fields = [];
    foreach ($_POST as $key => $value) {
        if (!$value) {
            $adding_error_fields[$key] = true;
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
        $query = "INSERT INTO `asterisk_users`(account_id, phone, balance) VALUES(?, ?, ?)";
        $stmt = mysqli_prepare($connection, $query);
        $stmt->bind_param('isi', $billing, $phone, $balance);
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