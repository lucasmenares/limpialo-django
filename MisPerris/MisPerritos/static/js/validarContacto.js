function validarNombre(){
    var nombre = document.querySelector("#inputNombre")
    if  (nombre.value.length >= 3 && nombre.value.length <= 50){
        return true;
    }
    else {        
        nombre.value = "";
        nombre.placeholder = "*Nombre entre 3 y 50 dígitos";
        nombre.classList.add("alertForm");
        return false;
    }
}

function validarApellido(){
    var apellido = document.querySelector("#inputApellido")
    if (apellido.value.length >= 3 && apellido.value.length <= 50){
        return true;
    }
    else {        
        apellido.value = "";
        apellido.placeholder = "*Apellido entre 3 y 50 dígitos";
        apellido.classList.add("alertForm");
        return false;
    }
}

function validarAsunto(){
    var asunto = document.querySelector("#inputAsunto")
    if (asunto.value.length >= 8 && asunto.value.length <= 50){
        return true;
    }
    else {
        asunto.value = "";
        asunto.placeholder = "*Asunto entre 8 y 50 dígitos";
        asunto.classList.add("alertForm");
        return false;
    }
}

function validarMensaje(){
    var mensaje = document.querySelector("#inputMensaje");
    if (mensaje.value.length >= 10 && mensaje.value.length <= 200){
        return true
    }
    else{
        mensaje.value = "";
        mensaje.placeholder = "*Mensaje entre 10 y 200 dígitos";
        mensaje.classList.add("alertForm");
        return false;
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
    if(validarAsunto()==false){
        resp = false;
    }
    if(validarMensaje()==false){
        resp = false;
    }
    if(resp == false){
        return false;
    }
    if(resp){
        document.querySelector("#formContacto").submit()
        return true;
    }

}

// Limpiar
function Limpiar(){
    // Resetea
    document.querySelector("#formContacto").reset();
    // Nombre
    document.querySelector("#inputNombre").classList.remove("alertForm");
    document.querySelector("#inputNombre").placeholder = "Nombre";
    // Apellido
    document.querySelector("#inputApellido").classList.remove("alertForm");
    document.querySelector("#inputApellido").placeholder = "Apellido";
    // Asunto
    document.querySelector("#inputAsunto").classList.remove("alertForm");
    document.querySelector("#inputAsunto").placeholder = "Asunto";
    // Mensaje
    document.querySelector("#inputMensaje").classList.remove("alertForm");
    document.querySelector("#inputMensaje").placeholder = "Mensaje";
}
