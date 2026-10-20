import { numero } from "../01-fundamentos/ejercicios.js";
export const maximo = (a, b) => Math.max(numero(a), numero(b));
export const promedio3 = (a, b, c) => (numero(a) + numero(b) + numero(c)) / 3;
export function promedioNotas(notas) {
  if (!notas.length) return null;
  return notas.map(numero).reduce((s, n) => s + n, 0) / notas.length;
}
export const siguiente = (n) => numero(n) + 1;
export const doble = (n) => numero(n) * 2;
export const cuadrado = (n) => numero(n) ** 2;
export const imprimirValores = (n) => ({
  siguiente: siguiente(n),
  doble: doble(n),
  cuadrado: cuadrado(n),
});
export const dobleDelSiguiente = (n) => doble(siguiente(n));
export const dobleDelSiguienteAlCuadrado = (n) => cuadrado(doble(siguiente(n)));
function dimension(n) {
  numero(n);
  if (n < 0) throw new RangeError("Dimensión no negativa");
  return n;
}
export const perimetroCuadrado = (lado) => 4 * dimension(lado);
export const superficieCuadrado = (lado) => dimension(lado) ** 2;
export const circunferencia = (radio) => 2 * Math.PI * dimension(radio);
export const areaCirculo = (radio) => Math.PI * dimension(radio) ** 2;
