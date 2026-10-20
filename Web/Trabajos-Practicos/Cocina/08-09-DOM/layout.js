const cabecera = `<nav class="navbar navbar-expand-sm navbar-dark" aria-label="Principal"><a class="navbar-brand" href="index.html">La cocina de Juan</a><button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#menu" aria-controls="menu" aria-expanded="false" aria-label="Abrir navegación"><span class="navbar-toggler-icon"></span></button><div class="collapse navbar-collapse" id="menu"><div class="navbar-nav ml-auto"><a class="nav-link" href="index.html">Carta</a><a class="nav-link" href="nosotros.html">Nosotros</a><a class="nav-link" href="contacto.html">Contacto</a></div></div></nav>`;
const pie = `<p>La cocina de Juan · HTML, Bootstrap y JavaScript</p><a href="../10-Vue/index.html">Continuar con Vue →</a>`;
document.querySelector("#cabecera").innerHTML = cabecera;
document.querySelector("#pie").innerHTML = pie;
const actual = location.pathname.split("/").pop() || "index.html";
document.querySelectorAll(".nav-link").forEach((a) => {
  if (a.getAttribute("href") === actual) {
    a.classList.add("active");
    a.setAttribute("aria-current", "page");
  }
});
