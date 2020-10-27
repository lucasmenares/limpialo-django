function validarNombreInsumos(){
    var nombreInsumos = document.querySelector("#inputNombre");
    if (nombreInsumos.value.length >= 3 && nombreInsumos.value.length <= 120) {
        return true;
    }
    else{
        nombreInsumos.value = "";
        nombreInsumos.classList.add('alertForm');
        nombreInsumos.placeholder = "*El nombre debe ser entre 3 y 120 carácteres";
        return false;
    }
}

function validarPrecio(){
    var precio = document.querySelector("#inputPrecio");
    if( precio.value >= 1) {
        return true;
    }
    else{
        precio.value = "";
        precio.classList.add('alertForm');
        precio.placeholder = "*Precio debe ser mayor a 1";
        return false;
    }
}

function validarDescripcion(){
    var descripcion = document.querySelector("#inputDescripcion");
        if (descripcion.value.length >= 3 && descripcion.value.length <= 200) {
            return true;
        }
        if(descripcion.value.length < 200){
            descripcion.value = "";
            descripcion.classList.add('alertForm');
            descripcion.placeholder = "*Descripción debe ser entre 3 y 200 carácteres";
            return false;
        }   
}


//-------------------------------------Validaciones Insumos----------------------------

function ValidarInsumos(){
    resp = true;
    if(validarNombreInsumos()== false){
        resp = false;
    }
    if (validarPrecio()==false){
        resp = false;
    }
    if(validarDescripcion()== false){
        resp = false;
    }

    if(resp){
        document.querySelector("#formInsumos").submit()
    }
}

// Limpiar
function Limpiar(){
    // Resetea
    document.querySelector("#formInsumos").reset();
    // Nombre
    document.querySelector("#inputNombre").classList.remove("alertForm");
    document.querySelector("#inputNombre").placeholder = "Nombre";
    // Precio
    document.querySelector("#inputPrecio").classList.remove("alertForm");
    document.querySelector("#inputPrecio").placeholder = "Precio";
    // Descripción
    document.querySelector("#inputDescripcion").classList.remove("alertForm");
    document.querySelector("#inputDescripcion").placeholder = "Descripción";
}