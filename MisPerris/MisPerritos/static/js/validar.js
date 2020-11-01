function validarNombre(){
    var nombre = document.querySelector("#inputNombre")
    if  (nombre.value.length >= 3 && nombre.value.length <= 80){
        return true;
    }
    else {        
        nombre.value = "";
        nombre.placeholder = "*Nombre entre 3 y 80 dígitos";
        nombre.classList.add("alertForm");
        return false;
    }
}

function validarApellido(){
    var apellido = document.querySelector("#inputApellido")
    if (apellido.value.length >= 3 && apellido.value.length <= 80){
        return true;
    }
    else {        
        apellido.value = "";
        apellido.placeholder = "*Apellido entre 3 y 80 dígitos";
        apellido.classList.add("alertForm");
        return false;
    }
}

function validarEmail(){
    var email = document.querySelector("#inputEmail")
    if (email.value.includes("@")){
        return true;
    }
    else {
        email.value = "";
        email.placeholder = "*Ingresa un email válido";
        email.classList.add("alertForm");
        return false;
    }
}

function validarUsuario(){
    var usuario = document.querySelector("#inputUsername");
    if (usuario.value.length < 8){
        usuario.value = "";
        usuario.placeholder = "*Nombre usuario 8 dígitos mínimo";
        usuario.classList.add("alertForm");
        return false;
    }
    else{
        return true;
    }
}

function validarContrasena(){
    var cont = document.querySelector("#inputPassword");
    var cont2 = document.querySelector("#inputPassword2");
    if (cont.value.length < 8 && cont2.value.length < 8){
        cont.value = "";
        cont.placeholder = "*Contraseña 8 dígitos mínimo";
        cont.classList.add("alertForm");
        return false;
    }
    else if(cont.value != cont2.value){
        cont.value = "";
        cont.placeholder = "*Contraseñas no coinciden";
        cont.classList.add("alertForm");
        cont2.value = "";
        cont2.placeholder = "*Contraseñas no coinciden";
        cont2.classList.add("alertForm");
        return false;
    }
    else{
        return true;
    }
}

//--------------------------------------Validaciones--------------------------------------------

function Validar(){
    var resp = true;
    if(validarNombre()== false){
        resp = false;
    }
    if(validarApellido()==false){
        resp = false;
    }
    if(validarEmail()==false){
        resp = false;
    }
    if(validarUsuario()==false){
        resp = false;
    }
    if(validarContrasena()==false){
        resp = false;
    }
    if(resp == false){
        return false;
    }
    if(resp){
        document.querySelector("#formUsuario").submit()
        return true;
    }

}

// Limpiar
function Limpiar(){
    // Resetea
    document.querySelector("#formUsuario").reset();
    // Nombre
    document.querySelector("#inputNombre").classList.remove("alertForm");
    document.querySelector("#inputNombre").placeholder = "Nombre";
    // Apellido
    document.querySelector("#inputApellido").classList.remove("alertForm");
    document.querySelector("#inputApellido").placeholder = "Apellido";
    // Email
    document.querySelector("#inputEmail").classList.remove("alertForm");
    document.querySelector("#inputEmail").placeholder = "Emaill";
    // Username
    document.querySelector("#inputUsername").classList.remove("alertForm");
    document.querySelector("#inputUsername").placeholder = "Nombre Usuario";
    // Password
    document.querySelector("#inputPassword").classList.remove("alertForm");
    document.querySelector("#inputPassword").placeholder = "Contraseña";
}
