function setErrorText(n) {
    console.log("gere");
    if(n == 1) {
        const username = document.getElementById("usernametext");
        username.innerText = "username is already taken";
    }
    if(n == 2) {
        const email = document.getElementById("emailtext");
        email.innerText = "email is already taken";
    }
    if(n == 3) {
        const password = document.getElementById("passwordtext");
        password.innerText = "password is invalid";
    }
}

function setErrorLogin(n) {
    console.log(n);
    if(n == 1) {
        const username = document.getElementById("usernametext");
        username.innerText = "username or password is incorrect";
    }
}
