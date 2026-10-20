const tareas = document.querySelector("#tareas");
const formulario = document.querySelector("#nueva-tarea");
formulario.addEventListener("submit", (event) => {
  event.preventDefault();
  const campo = formulario.elements.tarea;
  const texto = campo.value.trim();
  if (!texto) return;
  const li = document.createElement("li");
  const etiqueta = document.createElement("label");
  const casilla = document.createElement("input");
  casilla.type = "checkbox";
  etiqueta.append(casilla, document.createTextNode(" " + texto));
  const quitar = document.createElement("button");
  quitar.type = "button";
  quitar.textContent = "Quitar";
  quitar.addEventListener("click", () => {
    li.remove();
    campo.focus();
  });
  li.append(etiqueta, quitar);
  tareas.append(li);
  campo.value = "";
  campo.focus();
  document.querySelector("#estado").textContent = "Tarea agregada.";
});
const tema = document.querySelector("#tema");
try {
  tema.value = localStorage.getItem("cac-tema") || "claro";
} catch {}
document.documentElement.dataset.tema = tema.value;
tema.addEventListener("change", () => {
  document.documentElement.dataset.tema = tema.value;
  try {
    localStorage.setItem("cac-tema", tema.value);
  } catch {
    document.querySelector("#estado").textContent =
      "El navegador no permite guardar la preferencia.";
  }
});
