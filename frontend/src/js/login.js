function init()
{
    loginButton = document.getElementById("login-button");
    loginButton.addEventListener("click", onLogin);
}
window.addEventListener("load", init);

function onLogin()
{
    pseudo = document.getElementById("pseudo-field").innerHTML;
    password = document.getElementById("password-field").innerHTML;

    login(pseudo, password);
}

async function login(pseudo, password)
{
    let request =
    {
        userName: pseudo,
        password: password
    };

    await fetch("https://authentification.polytex.com/auth/login", {method : "POST", body: JSON.stringify(request)});
}