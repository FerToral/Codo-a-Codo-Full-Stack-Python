import { productos, filtrarProductos } from "../recursos/productos.js";
export const secciones = {
  inicio: "Inicio",
  carta: "Carta",
  nosotros: "Nosotros",
  contacto: "Contacto",
};
export function ruta(hash) {
  const clave = hash.replace(/^#/, "");
  return Object.hasOwn(secciones, clave) ? clave : "inicio";
}
const app = new Vue({
  el: "#app",
  data: {
    secciones,
    seccion: ruta(location.hash),
    productos,
    busqueda: "",
    categoria: "Todas",
    nombre: "",
    correo: "",
    mensaje: "",
    estado: "",
  },
  computed: {
    filtrados() {
      return filtrarProductos(this.productos, this.busqueda, this.categoria);
    },
  },
  methods: {
    validar() {
      this.estado =
        "Mensaje válido. Ejemplo local: no se realizó ningún envío.";
    },
  },
});
window.addEventListener("hashchange", () => {
  app.seccion = ruta(location.hash);
  app.$nextTick(() => {
    const titulo = document.querySelector("main h1");
    titulo.tabIndex = -1;
    titulo.focus();
    document.title = `${secciones[app.seccion]} · La cocina de Juan`;
  });
});
