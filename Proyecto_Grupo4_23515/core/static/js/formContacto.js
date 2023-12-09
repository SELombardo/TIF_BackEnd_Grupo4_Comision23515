const contactForm = document.getElementById("contactForm");

contactForm.addEventListener("submit", (event) => {
  event.preventDefault();
  var nombre = document.getElementById("nombre").value;
  var apellido = document.getElementById("apellido").value;
  var email = document.getElementById("email").value;
  var mensaje = document.getElementById("mensaje").value;

  if (nombre.length < 3) {
    alert("Por favor, ingrese su nombre.");
    return false;
  }
  if (apellido.length < 3) {
    alert("Por favor, ingrese su apellido.");
    return false;
  }
  if (email.length < 4) {
    alert("Por favor, ingrese su correo electrónico.");
    return false;
  }
  if (mensaje.length < 4) {
    alert("Por favor, ingrese su mensaje");
    return false;
  }

  contactForm.reset();

  return alert("El formulario fue enviado correctamente");
});
