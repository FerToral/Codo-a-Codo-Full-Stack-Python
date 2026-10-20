export const productos = [
  {
    codigo: "P01",
    imagen: "../recursos/plato.svg",
    nombre: "Ensalada de estación",
    descripcion: "Hojas verdes, tomate, huevo y pan tostado.",
    categoria: "Vegetariano",
    minutos: 15,
  },
  {
    codigo: "P02",
    imagen: "../recursos/tarta.svg",
    nombre: "Tarta de verduras",
    descripcion: "Masa casera con zapallito, cebolla y queso.",
    categoria: "Vegetariano",
    minutos: 45,
  },
  {
    codigo: "P03",
    imagen: "../recursos/arroz-pollo.svg",
    nombre: "Arroz con pollo",
    descripcion: "Una receta de olla con arroz, pollo y verduras.",
    categoria: "Con carne",
    minutos: 35,
  },
  {
    codigo: "P04",
    imagen: "../recursos/lentejas.svg",
    nombre: "Guiso de lentejas",
    descripcion: "Lentejas, calabaza y pimentón, sin ingredientes animales.",
    categoria: "Vegano",
    minutos: 40,
  },
  {
    codigo: "P05",
    imagen: "../recursos/sopa.svg",
    nombre: "Sopa de calabaza",
    descripcion: "Calabaza asada, caldo de verduras y semillas.",
    categoria: "Vegano",
    minutos: 30,
  },
  {
    codigo: "P06",
    imagen: "../recursos/pasta.svg",
    nombre: "Pasta con tomate",
    descripcion: "Pasta corta, salsa de tomate y albahaca fresca.",
    categoria: "Vegetariano",
    minutos: 25,
  },
];
export function filtrarProductos(lista, texto = "", categoria = "Todas") {
  const consulta = texto.trim().toLocaleLowerCase("es");
  return lista.filter(
    (p) =>
      (categoria === "Todas" || p.categoria === categoria) &&
      `${p.nombre} ${p.descripcion}`.toLocaleLowerCase("es").includes(consulta),
  );
}
