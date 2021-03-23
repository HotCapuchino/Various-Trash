<?php 

    function connect_to_db() {
        $connection = mysqli_connect('localhost', 'test_user', 'Big_test1', 'test');
        if (mysqli_connect_error()) {
            return false;
        }
        return $connection;
    }
