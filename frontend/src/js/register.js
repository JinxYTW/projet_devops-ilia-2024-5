function init()
{
    loginButton = document.getElementById("login-button");
    loginButton.addEventListener("click", onRegister);
}
window.addEventListener("load", init);

function onRegister()
{
    firstName = document.getElementById("first-name-field").innerHTML;
    lastName = document.getElementById("last-name-field").innerHTML;

    email = document.getElementById("email-field").innerHTML;
    pseudo = document.getElementById("pseudo-field").innerHTML;

    password = document.getElementById("password-field").innerHTML;

    register(firstName, lastName, email, pseudo, password);
}

async function register(firstName, lastName, email, pseudo, password)
{
    let request =
    {
        firstName: firstName,
        lastName: lastName,
        email: email,
        userName: pseudo,
        password: password
    };

    await fetch("https://authentification.polytex.com/auth/sign_in", {method : "POST", body: JSON.stringify(request)});
}