<?php
session_start();

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    //Връзки
    $conn = new mysqli("127.0.0.1", "pesho", "parola", "lms2");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Данни 
    $sql = "SELECT id, username, password FROM users WHERE username = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();

        // Потвърждаване на парола
        if (password_verify($password, $row["password"])) {
            $_SESSION["user_id"] = $row["id"];
            $_SESSION["username"] = $row["username"];
            header("Location: /index/index.html"); // Прехвърляне
            exit();
        } else {
            echo "Incorrect password. <a href='/log-in/log-in.html'>Try again</a>.";
        }
    } else {
        echo "User not found. <a href='/sign-up/sign-up.html'>Sign up</a> if you don't have an account.";
    }

    $stmt->close();
    $conn->close();
    
}
?>
