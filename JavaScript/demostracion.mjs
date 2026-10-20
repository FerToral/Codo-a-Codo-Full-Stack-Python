import * as funciones from "./02-funciones/ejercicios.js";
import * as arrays from "./03-arrays-y-cadenas/ejercicios.js";

const entradaNotas = [6, 8, 10, -1, 2];
const fin = entradaNotas.indexOf(-1);
const notas = fin < 0 ? entradaNotas : entradaNotas.slice(0, fin);
console.log("Promedio hasta -1:", funciones.promedioNotas(notas));
console.log("Composición para 3:", funciones.dobleDelSiguienteAlCuadrado(3));
console.log(
  "Cuadrado de lado 4:",
  funciones.perimetroCuadrado(4),
  funciones.superficieCuadrado(4),
);
console.log(
  "Círculo de radio 2:",
  funciones.circunferencia(2),
  funciones.areaCirculo(2),
);
const valores = [
  3, 6, 67, 6, 23, 11, 100, 8, 93, 0, 17, 24, 7, 1, 33, 45, 28, 33, 23, 12, 99,
  100,
];
console.log("Menor y mayor:", arrays.minimo(valores), arrays.maximo(valores));
console.log("Repetidos:", arrays.repetidos(valores));
console.log("Posición 2:", arrays.enPosicion(valores, 2));
console.log("Colores:", arrays.unir(["Red", "Green", "White", "Black"]));
console.log("Dígitos invertidos:", arrays.invertirNumero(32443));
console.log("Letras ordenadas:", arrays.alfabetico("webmaster"));
console.log("Iniciales:", arrays.titulo("curso de desarrollo web"));
console.log(
  "Palabra más larga:",
  arrays.palabraMasLarga("Curso de desarrollo web"),
);
