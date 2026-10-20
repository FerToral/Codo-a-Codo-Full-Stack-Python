import { entero, numero } from "../01-fundamentos/ejercicios.js";
export function recorrerWhile(edades) {
  const salida = [];
  let i = 0;
  while (i < edades.length) salida.push(numero(edades[i++]));
  return salida;
}
export function paresFor(edades) {
  const salida = [];
  for (let i = 0; i < edades.length; i++)
    if (entero(edades[i]) % 2 === 0) salida.push(edades[i]);
  return salida;
}
function extremo(valores, menor) {
  if (!valores.length) throw new RangeError("El array no puede estar vacío");
  let resultado = numero(valores[0]);
  for (let i = 1; i < valores.length; i++) {
    const actual = numero(valores[i]);
    if (menor ? actual < resultado : actual > resultado) resultado = actual;
  }
  return resultado;
}
export const minimo = (valores) => extremo(valores, true);
export const maximo = (valores) => extremo(valores, false);
export function enPosicion(valores, posicion) {
  entero(posicion);
  if (posicion < 1 || posicion > valores.length)
    throw new RangeError("Posición de 1 a longitud");
  return valores[posicion - 1];
}
export function repetidos(valores) {
  const cantidades = new Map();
  for (const valor of valores)
    cantidades.set(valor, (cantidades.get(valor) || 0) + 1);
  return [...cantidades].filter(([, n]) => n > 1).map(([valor]) => valor);
}
export const unir = (colores) => colores.join(", ");
export function invertirNumero(n) {
  entero(n);
  const signo = Math.sign(n);
  const resultado =
    Number(String(Math.abs(n)).split("").reverse().join("")) * signo;
  entero(resultado);
  return resultado;
}
export const alfabetico = (palabra) =>
  [...palabra].sort((a, b) => a.localeCompare(b, "es")).join("");
export const titulo = (frase) =>
  frase.replace(/\S+/gu, (p) => p[0].toLocaleUpperCase("es") + p.slice(1));
export function palabraMasLarga(frase) {
  return (frase.match(/[\p{L}\p{N}]+/gu) || []).reduce(
    (larga, p) => (p.length > larga.length ? p : larga),
    "",
  );
}
