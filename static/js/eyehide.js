function togglePasswordVisibility() {
    var passwordInput = document.getElementById("passwordInput");
    var toggleButton = document.getElementById("eyeIcon");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.src = "/static/img/view.png";
    } else {
        passwordInput.type = "password";
        toggleButton.src = "/static/img/hide.png";
    }
}
function togglePasswordVisibilityTwo() {
    var passwordInput = document.getElementById("passwordInputTwo");
    var toggleButton = document.getElementById("eyeIconTwo");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleButton.src = "/static/img/view.png";
    } else {
        passwordInput.type = "password";
        toggleButton.src = "/static/img/hide.png";
    }
}

function PassRequirements (){
    var passwordInput = document.getElementById("passwordInput").value;
    var caracterEspecial = /[-!$%^&*()_+|~=`{}\[\]:";'<>?,.\/]/;
    var submitButton = document.querySelector("#SignUp button[type='submit']");


    if(passwordInput.length >= 8){
        document.getElementById("requirements0").style.color="green";
    }
    else{

        document.getElementById("requirements0").style.color="red";
    }

    if(caracterEspecial.test(passwordInput)){
        document.getElementById("requirements1").style.color="green";
    }
    else{
        document.getElementById("requirements1").style.color="red";

    }
    if(caracterEspecial.test(passwordInput) && passwordInput.length >= 8){
        submitButton.disabled = false;
    }
    else{
        submitButton.disabled = true;
    }

}
