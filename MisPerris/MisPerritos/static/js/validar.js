function validarRut(){
    var rut = document.querySelector("#inputRut");
    if (rut.value.length == 9) {
        rut.value = "";
        rut.placeholder = "*Si tu rut tiene 9 dígitos pon un 0 al principio";
        rut.classList.add("alertForm");
        return false;
    }
    else if(rut.value.length != 10){
        rut.value = "";
        rut.placeholder = "*El rut debe tener 10 dígitos";
        rut.classList.add("alertForm");
        return false;
    }
    else if(!rut.value.includes("-")){
        rut.value = "";
        rut.placeholder = "*El rut debe contener guión";
        rut.classList.add("alertForm");
        return false;
    }
    var suma = 0;
    var num = 3;
    for (var index = 0; index < 8; index++) {
        var car = rut.value.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.value.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        rut.value = "";
        rut.placeholder = "*Rut inválido";
        rut.classList.add("alertForm");
        return false;
    } else {
        return true;
    }
}

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
    if (cont.value.length < 8){
        cont.value = "";
        cont.placeholder = "*Contraseña 8 dígitos mínimo";
        cont.classList.add("alertForm");
    }
}

function validarFecha(){
    var fecha = document.querySelector("#inputFecha")
    var fechaSistema = new Date();
    var alertFecha = document.querySelector("#pFecha");

    var ano = fecha.value.slice(0, 4);
    var mes = fecha.value.slice(5, 7);
    var dia = fecha.value.slice(8, 10);

    var fechaDelControl = new Date(ano, (mes - 1), dia);
    if (fechaDelControl > fechaSistema || fecha.value.length == 0 ) {;
        alertFecha.innerHTML = "*Ingresa una fecha válida";
        return false;
    } else {
        if(alertFecha.value != ""){
            alertFecha.innerHTML = "";
        }
        return true;
    }
}

//--------------------------------------Validaciones--------------------------------------------

function Validar(){
    var resp = true;
    if (validarRut() == false) {
        resp = false;
    }
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
    if(validarFecha()==false){
        resp = false;
    }
    
    if(resp){
        document.querySelector("#formUsuario").submit()
    }

}

// Limpiar
function Limpiar(){
    // Resetea
    document.querySelector("#formUsuario").reset();
    // Rut
    document.querySelector("#inputRut").classList.remove("alertForm");
    document.querySelector("#inputRut").placeholder = "Rut (Ejemplo: 01111111-1";
    // Nombre
    document.querySelector("#inputNombre").classList.remove("alertForm");
    document.querySelector("#inputNombre").placeholder = "Nombre";
    // Apellido
    document.querySelector("#inputApellido").classList.remove("alertForm");
    document.querySelector("#inputApellido").placeholder = "Apellido";
    // Email
    document.querySelector("#inputEmail").classList.remove("alertForm");
    document.querySelector("#inputEmail").placeholder = "Emaill";
    // Fecha
    document.querySelector("#pFecha").innerHTML = "";
    // Username
    document.querySelector("#inputUsername").classList.remove("alertForm");
    document.querySelector("#inputUsername").placeholder = "Nombre Usuario";
    // Password
    document.querySelector("#inputPassword").classList.remove("alertForm");
    document.querySelector("#inputPassword").placeholder = "Contraseña";
}
