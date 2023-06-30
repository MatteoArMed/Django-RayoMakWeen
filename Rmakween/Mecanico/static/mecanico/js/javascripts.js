
// Variables pagina 'Registro'
var usuario = document.getElementById('usuario');
var emailUsuario = document.getElementById('emailUsuario');
var contrasenna = document.getElementById('contrasenna');

//funcion de crear usuario y validacion 
function crearUsuario(){
	if(usuario.value === '' || usuario.value === null){
		alert('Debes ingresar un nombre de usuario')
		return false;
	}
	if(emailUsuario.value === '' || emailUsuario.value === null){
		alert('Debes ingresar un correo')
		return false;
	}
	if(contrasenna.value === '' || contrasenna.value === null){
		alert('Debes ingresar una contraseña')
		return false;
	}

	document.getElementById('crearUsuario').submit();
    return true;
}


// variables pagina 'Inicio Sesion'
var loginUsuario = document.getElementById('loginUsuario');
var loginContrasenna = document.getElementById('loginContrasenna');
//funcion de validacion de login
function validaLogin(){
	if(loginUsuario.value === '' || loginUsuario.value === null){
		alert('Debes ingresar un usuario')
		return false;
	}
	if(loginContrasenna.value === '' || loginContrasenna.value === null){
		alert('Debes ingresar una contraseña')
		return false
	}

	document.getElementById('iniciarSesion').submit();
    return true;
}



// Variables formulario 'Contacto'
var nombreContacto = document.getElementById('nombreContacto');
var emailContacto = document.getElementById('emailContacto');
var numeroContacto = document.getElementById('numeroContacto');
var descripcionProblema = document.getElementById('descripcionProblema');


function EnviarFormularioContacto(){
    
    if(nombreContacto.value === null || nombreContacto.value === ''){
        alert('Debes ingresar un nombre');
		return false;
    }
	
    if(emailContacto.value === '' || emailContacto.value === null){
		alert('Debes ingresar un correo');
		return false;

    } else if (!/^[\w.-]+@[\w.-]+\.\w+$/.test(emailContacto.value)){
		alert('Debes ingresar un correo válido');
		return false;
	}
	
	if(numeroContacto.value === null || numeroContacto.value === ''){
		alert('Debes ingresar un número de telefóno')
		return false;
	} else if (numeroContacto.value.length === 12){

	} else {
		alert('Debes ingresar un número valido')
		return false;
	} 
			
	if(descripcionProblema.value === null || descripcionProblema.value === ''){
		alert('Por favor, cuentanos cual es tu duda')
		return false;
	}

	document.getElementById('contacto').submit();
    return true;
}


// Filtros de los trabajos

function aplicarFiltro() {
	var selectedOption = document.getElementById("opciones").value;
	var rows = document.querySelectorAll("table tbody tr");

	rows.forEach(function(row) {
	var mecanicoCell = row.querySelector(".align-middle:nth-child(2)");
	if (selectedOption !== "todos" && mecanicoCell.innerHTML !== selectedOption) {
		row.style.display = "none";
	} else {
		row.style.display = "table-row";
	}
	});
}

