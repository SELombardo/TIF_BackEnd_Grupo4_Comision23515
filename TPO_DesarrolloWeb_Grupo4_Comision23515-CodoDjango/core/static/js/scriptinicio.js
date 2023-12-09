// CUADRO DE MENSAJES ALEATORIOS

const mensajes = [
  '"El gimnasio es el lugar donde tus metas se vuelven posibles. ¡Sigue adelante y alcanza tus objetivos"',
  '"Cada día en el gimnasio es un paso más cerca de ser la mejor versión de ti mismo. ¡No pares ahora!"',
  '"El dolor que sientes hoy será la fuerza que sientas mañana. ¡Sigue entrenando con determinación!"',
  '"Tu cuerpo es tu proyecto más importante. Invierte tiempo en él, ¡los resultados valen la pena"',
  '"El gimnasio no solo transforma tu cuerpo, también fortalece tu mente. ¡Mantén una actitud positiva y nunca te rindas!"',
];

let mensajeActual = 0;

function mostrarMensaje() {
  const mensajeContainer = document.getElementById("mensaje-container");
  mensajeContainer.textContent = mensajes[mensajeActual];

  mensajeActual++;

  if (mensajeActual === mensajes.length) {
    mensajeActual = 0;
  }

  setTimeout(mostrarMensaje, 4000);
}

mostrarMensaje();
