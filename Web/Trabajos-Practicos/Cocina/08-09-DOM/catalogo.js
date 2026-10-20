import { productos, filtrarProductos } from "../recursos/productos.js";
const lista = document.querySelector("#productos");
function mostrar() {
  const encontrados = filtrarProductos(
    productos,
    document.querySelector("#buscar").value,
  );
  lista.replaceChildren();
  for (const p of encontrados) {
    const articulo = document.createElement("article");
    articulo.className = "plato";
    const imagen = document.createElement("img");
    imagen.src = p.imagen;
    imagen.alt = "";
    const titulo = document.createElement("h2");
    titulo.textContent = p.nombre;
    const descripcion = document.createElement("p");
    descripcion.textContent = p.descripcion;
    const datos = document.createElement("p");
    datos.className = "datos";
    datos.textContent = `${p.codigo} · ${p.categoria} · ${p.minutos} min`;
    articulo.append(imagen, titulo, descripcion, datos);
    lista.append(articulo);
  }
  document.querySelector("#cantidad").textContent =
    `${encontrados.length} platos`;
}
document.querySelector("#buscar").addEventListener("input", mostrar);
mostrar();
