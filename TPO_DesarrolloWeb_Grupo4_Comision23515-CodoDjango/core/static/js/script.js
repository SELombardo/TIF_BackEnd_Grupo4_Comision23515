/* TARJETAS ACTIVIDADES */

const containerActiv = document.querySelector(".containerActiv");

//Solicita el archivo .json mediante la función fetch()
fetch('/static/database.json')
//Cuando se reciba una respuesta (response) de fetch, convierte esa respuesta a formato JSON mediante la función .json().

.then((response) => response.json()) 
// Cuando la conversión a JSON se complete, ejecuta una función que recibe el objeto JSON en formato JavaScript como argumento.

.then((data) => {
  //Bucle de iteración
  for (const actividad of data) {
    //Crea elementos HTML en el documento y los agrega al contenedor productContainer
    containerActiv.innerHTML +=
      `
      <div class="cardActiv"> 
          <div class="face front">
              <img src=${actividad.img} alt="imágen de ejercitación ${actividad.actividad}">
              <h3>${actividad.actividad}</h3>
          </div>   
          <div class="face back">
              <h3>${actividad.actividad}</h3>
              <p>${actividad.días}</p>
              <p>${actividad.horarios} h</p>
          </div>
        </div>
      `;
  }
})


