// Para el Registro
function validarFormulario() {
  
  var nombre = document.getElementById("nombre").value;
  var apellido = document.getElementById("apellido").value;
  var email = document.getElementById("mail").value;
  var telefono = document.getElementById("fono").value;
  var contraseña1 = document.getElementById("contraseña1").value;
  var contraseña2 = document.getElementById("contraseña2").value;
  
  // Validar que todos los campos estén completos.
  if (nombre === "" || apellido === "" || email === "" || telefono === "" || contraseña1 === "" || contraseña2 === "") {
    alert("Por favor, complete todos los campos del formulario");
    return false;
  }
  
  // Validar que la primera y segunda contraseña coincidan.
  if (contraseña1 !== contraseña2) {
    alert("Las contraseñas no coinciden 😬");
    return false;
  }
 
  return true;
}


// Para el Login. Usuario: asd / Contraseña: asd
function validarInicioSesion() {
  var usuario = document.querySelector('.i1').value;
  var contraseña = document.querySelector('.i2').value;

  if (usuario === '' || contraseña === '') {
    alert('Por favor ingresa un usuario y una contraseña válidos');
    return false;
  }else if (usuario === 'asd' && contraseña === 'asd'){
    return true;
  }else{
    alert('Por favor ingresa un usuario y una contraseña válidos');
    return false;
  }
  return true;
}

//modal popup index
