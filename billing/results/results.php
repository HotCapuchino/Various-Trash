<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../general.css">
    <title>Document</title>
</head>
<body>
    <div class="general-wrapper">
        <?php 
            if (isset($connect_error)) {
                echo '<h1>Cannot establish connection to database!</h1>';
            } 
            if (isset($success)) {
                if (!$success) {
                    echo '<h1>Operation failed!</h1>';
                } else {
                    echo '<h1>Operation successful!</h1>';
                }
            }
        ?>
        <a href="../index.php">Main page</a>
    </div>
</body>
</html>