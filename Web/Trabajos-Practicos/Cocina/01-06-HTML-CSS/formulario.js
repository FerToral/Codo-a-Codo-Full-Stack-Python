const formulario = document.querySelector("#registro");
const estado = document.querySelector("#estado");
const resumen = document.querySelector("#resumen");
const datosResumen = document.querySelector("#datos-resumen");
const nombres = {
  nombre: "Nombre",
  apellido: "Apellido",
  correo: "Correo",
  telefono: "Teléfono",
  nacimiento: "Fecha",
  calle: "Calle",
  numero: "Número",
  ciudad: "Ciudad",
  postal: "Código postal",
  genero: "Género",
  conocimientos: "Conocimientos",
  estudios: "Estudios",
  enlace: "Enlace",
  comentarios: "Comentarios",
};
formulario?.addEventListener("submit", (evento) => {
  evento.preventDefault();
  if (!formulario.checkValidity()) {
    estado.textContent = "Revisá los campos señalados.";
    formulario.reportValidity();
    return;
  }
  datosResumen.replaceChildren();
  for (const [nombre, valor] of new FormData(formulario)) {
    if (nombre === "clave" || !valor) continue;
    const termino = document.createElement("dt");
    const definicion = document.createElement("dd");
    termino.textContent = nombres[nombre] || nombre;
    definicion.textContent = valor;
    datosResumen.append(termino, definicion);
  }
  resumen.hidden = false;
  formulario.elements.clave.value = "";
  estado.textContent = "Resumen preparado. No se enviaron ni guardaron datos.";
  document.querySelector("#titulo-resumen").focus();
});
