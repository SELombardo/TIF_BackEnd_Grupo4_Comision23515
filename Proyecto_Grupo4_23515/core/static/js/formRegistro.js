// const regisForm = document.getElementById("regisForm");

// regisForm.addEventListener("submit", (e) => {
//   e.preventDefault();

//   var nombre = document.getElementById("nombre_regis").value;
//   var apellido = document.getElementById("apellido_regis").value;
//   var dni = document.getElementById("dni_regis").value;
//   var email = document.getElementById("email_regis").value;
//   var tel = document.getElementById("tel_regis").value;

//   if (nombre.length < 3) {
//     alert("Por favor, ingrese su nombre.");
//     return false;
//   }
//   if (apellido.length < 3) {
//     alert("Por favor, ingrese su apellido.");
//     return false;
//   }
//   if (dni.length < 8 || isNaN(dni)){
//     alert("Por favor, ingrese su DNI");
//     return false;
//   }
//   if (email.length < 4) {
//     alert("Por favor, ingrese su correo electrónico.");
//     return false;
//   }
//   if (tel.length < 10 || isNaN(tel)) {
//     alert("Por favor, ingrese su teléfono");
//     return false;
//   }

//   //regisForm.reset();

//   return alert("Usted se ha registrado correctamente");
  
// })