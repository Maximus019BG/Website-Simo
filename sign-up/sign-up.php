<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // Парола
    $hashedPassword = password_hash($password, PASSWORD_DEFAULT);

    // Връзки
    $conn = new mysqli("127.0.0.1", "pesho", "parola", "lms2");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }

    // Име
    $checkUsernameQuery = "SELECT * FROM users WHERE username = ?";
    $stmt = $conn->prepare($checkUsernameQuery);
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();
    if ($result->num_rows > 0) {
        echo "Username is already taken. Please choose another one.";
    } else {
        //Данни
        $insertQuery = "INSERT INTO users (username, password) VALUES (?, ?)";
        $stmt = $conn->prepare($insertQuery);
        $stmt->bind_param("ss", $username, $hashedPassword);
        if ($stmt->execute()) {
            echo "Registration successful. You can now <a href='/log-in/log-in.html'>log in</a>.";//Прехвърляне
       
        } else {
            echo "Error: " . $stmt->error;
        }
    }

    $stmt->close();
    $conn->close();
    
}
?>

