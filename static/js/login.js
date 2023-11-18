document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var username = document.getElementById('username').value;
    var password = document.getElementById('password').value;

    if (username === "" || password === "") {
        alert("Please enter both username and password");
        return false;
    }
    // Redirect to another page or perform other actions after login
    
    return true;
});