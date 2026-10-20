// Demostración local: no enviar, persistir ni registrar los campos.
const form = document.querySelector("#contacto");
form?.addEventListener("submit", (event) => {
  event.preventDefault();
  const status = document.querySelector("#estado-contacto");
  if (!form.checkValidity()) {
    form.reportValidity();
    status.textContent = "Revisá los campos requeridos.";
    return;
  }
  status.textContent =
    "Formulario válido. Es una demostración: no se enviaron ni guardaron tus datos.";
});
