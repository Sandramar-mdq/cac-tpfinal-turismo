let nombre = document.getElementById('nombre');
let apellido = document.getElementById('apellido');
let telefono = document.getElementById('telefono');
let email = document.getElementById('email');
let error = document.getElementById('error');
error.style.color = red;

let validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
let validNom = /^([a-z ñáéíóú]{2,60})$/i;
let validApe = /^([a-z ñáéíóú]{2,60})$/i;



function validarForm() {
    console.log('Enviando formulario...');
    
    let mensajesError = [];

    
    if(nombre.value === null || nombre.value === '' || validNom.value(nombre.value)){
        mensajesError.push('Ingresa tu nombre');
    }

    if(apellido.value === null || apellido.value === '' || validApe.value(apellido.value)){
        mensajesError.push('Ingresa tu apellido');
    }
    
    if(isNaN(telefono) || (/^\d{10}$/.test(telefono))){
        mensajesError.push('Ingresa un número de tel. válido');
    }

    if(validEmail.value(email.value) ){
        mensajesError.push('Ingresa un correo electrónico válido');
    }

    //convierte el erreglo a string
    error.innerHTML = mensajesError.join(', ');

    return false;

}