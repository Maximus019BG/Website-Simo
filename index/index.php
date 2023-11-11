<?php
session_start();

// Check if the user is logged in
if (isset($_SESSION['user_id'])) {
    // Връзки
    $conn = new mysqli("127.0.0.1", "pesho", "parola", "lms2");

    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    // User is logged in
    $loginLinkText = "Liked"; // Change the text for logged-in users
} else {
    // User is not logged in
    $loginLinkText = "Sign in"; // Default text for login link
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST["username"];
    $password = $_POST["password"];

    // ... (your existing login logic)

    if (isset($_SESSION['user_id'])) {
        // User successfully logged in
        $loginLinkText = "Liked"; // Change the text for logged-in users after login
    }
}
?>