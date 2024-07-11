function guardar() {
    let nombre_ingresado = document.getElementById("nombre").value //input
    let apellido_ingresado = document.getElementById("apellido").value 
    let telefono_ingresado = document.getElementById("telefono").value 
    let mail_ingresado = document.getElementById("mail").value 
    let foto_dni_ingresada = document.getElementById("foto_dni").value 

    console.log(nombre_ingresado,apellido_ingresado,telefono_ingresado,mail_ingresado, foto_dni_ingresada);
    // Se arma el objeto de js 
    let datos = {
        nombre: nombre_ingresado,
        apellido:apellido_ingresado,
        telefono:telefono_ingresado,
        mail:mail_ingresado,
        foto_dni:foto_dni_ingresada
    }
    
    console.log(datos);
    
    let url = "http://localhost:5000/registro"
    var options = {
        body: JSON.stringify(datos),
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
    }

    fetch(url, options)
        .then(function () {
            console.log("creado")
            alert("Grabado")
            // Devuelve el href (URL) de la página actual
            window.location.href = "../tabla_clientes.html";  
            
        })

        .catch(err => {
            //this.errored = true
            alert("Error al grabar" )
            console.error(err);
        })
}