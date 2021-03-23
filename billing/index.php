<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="general.css">
    <title>Document</title>
</head>
<body>
    <div class="general-wrapper">
        <form action="operations/add_user.php" method="POST" class="add-form">
            <h2>Here you can add new user</h2>
            <label>
                Billing number
                <input type="number" name="billing" placeholder="billing">
                <?php 
                    if ($adding_error_fields['billing']) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    } 
                ?>
            </label>
            <label>
                Phone number
                <input type="text" name="phone" placeholder="phone">
                <?php 
                    if ($adding_error_fields['phone']) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    }
                ?>
            </label>
            <label>
                User balance
                <input type="number" name="balance" placeholder="balance">
                <?php 
                    if ($adding_error_fields['balance']) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    }
                ?>
            </label>
            <button>Add user</button>
        </form>
        <form action="operations/delete_user.php" method="POST" class="delete-form">

            <h2>Here you can delete user</h2>
            <label>
                Billing number
                <input type="number" name="billing" placeholder="delte billing number">
                <?php 
                    if ($deleting_error) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    } 
                ?>
            </label>
            <button>Delete user</button>
        </form>
        <form action="operations/update_user.php" method="POST" class="update-form">
            <h2>Here you can update phone and balance</h2>
            <label>
                Billing number
                <input type="number" name="billing" placeholder="find billing number">
                <?php 
                    if ($updating_error_fields['billing']) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    } 
                ?>
            </label>
            <label>
                Phone number
                <input type="text" name="phone" placeholder="change phone">
                <?php 
                    if ($updating_error_fields['phone']) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    } 
                ?>
            </label>
            <label>
                User balance
                <input type="number" name="balance" placeholder="change balance">
                <?php 
                    if ($updating_error_fields['balance']) {
                        echo '<p class="error-field">This field should not be empty!</p>';
                    } 
                ?>
            </label>
            <button>Update user</button>
        </form>
    </div>
</body>
</html>