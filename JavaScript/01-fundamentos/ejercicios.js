/** Guía de clase 14: expresiones, decisiones, cadenas y ciclos. */
export function numero(valor) {
  if (typeof valor !== "number" || !Number.isFinite(valor))
    throw new TypeError("Se necesita un número finito");
  return valor;
}
export function entero(valor) {
  numero(valor);
  if (!Number.isSafeInteger(valor))
    throw new RangeError("Se necesita un entero seguro");
  return valor;
}
export function vocales(frase) {
  return Object.fromEntries(
    [..."aeiou"].map((v) => [
      v,
      [...frase.toLowerCase()].filter((c) => c === v).length,
    ]),
  );
}
export function divisores(n) {
  entero(n);
  if (!n) throw new RangeError("Cero tiene infinitos divisores");
  n = Math.abs(n);
  const resultado = [];
  for (let i = 1; i <= Math.sqrt(n); i++)
    if (n % i === 0) {
      resultado.push(i);
      if (i * i !== n) resultado.push(n / i);
    }
  return resultado.sort((a, b) => a - b);
}
export function esPrimo(n) {
  entero(n);
  if (n < 2) return false;
  for (let d = 2; d * d <= n; d++) if (n % d === 0) return false;
  return true;
}
export function calificacion(nota) {
  numero(nota);
  if (nota < 0 || nota > 10) throw new RangeError("Nota entre 0 y 10");
  for (const [tope, texto] of [
    [3, "Muy deficiente"],
    [5, "Insuficiente"],
    [6, "Suficiente"],
    [7, "Bien"],
    [9, "Notable"],
  ])
    if (nota < tope) return texto;
  return "Sobresaliente";
}
export function letraDni(n) {
  entero(n);
  if (n < 0 || n > 99999999) throw new RangeError("DNI entre 0 y 99999999");
  return "TRWAGMYFPDXBNJZSQVHLCKE"[n % 23];
}
export function piramide(n, { inversa = false, acumulativa = false } = {}) {
  entero(n);
  if (n < 1 || n > 50) throw new RangeError("Altura entre 1 y 50");
  const filas = [];
  for (let i = 1; i <= n; i++)
    filas.push(
      acumulativa
        ? Array.from({ length: i }, (_, j) => j + 1).join("")
        : String(i).repeat(i),
    );
  return inversa ? filas.reverse() : filas;
}
export function multiplosHasta(limite = 500) {
  const filas = [];
  for (let n = 1; n <= limite; n++) {
    const etiquetas = [4, 9]
      .filter((d) => n % d === 0)
      .map((d) => `Múltiplo de ${d}`);
    filas.push(
      String(n) + (etiquetas.length ? " (" + etiquetas.join(", ") + ")" : ""),
    );
    if (n % 5 === 0) filas.push("────────────────────");
  }
  return filas;
}
export const actividades = [
  ["Saludo con alert", []],
  ["Salida con document.write", []],
  ["Suma 3 + 5", []],
  ["Saludo por nombre", ["Ana"]],
  ["Suma de dos números", [3, 5]],
  ["Mayor de dos", [4, 2]],
  ["Mayor de tres", [4, 9, 2]],
  ["Divisible por dos", [8]],
  ["Apariciones de a", ["La casa"]],
  ["Vocales presentes", ["Murciélago"]],
  ["Cantidad de vocales", ["Una frase"]],
  ["Frecuencia de cada vocal", ["Una frase"]],
  ["Divisible por 2, 3, 5 o 7", [30]],
  ["Todos los divisores entre 2, 3, 5 y 7", [30]],
  ["Divisores de un entero", [24]],
  ["Divisores comunes", [12, 18]],
  ["Número primo", [17]],
  ["Edad mayor de 18", [19]],
  ["Calificación", [7]],
  ["Textos concatenados", [["uno", "dos"]]],
  ["Suma validada", [[2, "error", 3]]],
  ["Letra del DNI español", [12345678]],
  ["Pirámide 1–30", []],
  ["Pirámide inversa", [6]],
  ["Pirámide acumulativa (alternativa)", [6]],
  ["Múltiplos y separadores", []],
];
export function resolver(id, datos = []) {
  const [a, b, c] = datos;
  if ([1, 2].includes(id)) return "Hello World";
  if (id === 3) return 3 + 5;
  if (id === 4) return "Hola " + String(a);
  if (id === 5) return numero(a) + numero(b);
  if (id === 6) return Math.max(numero(a), numero(b));
  if (id === 7) return Math.max(numero(a), numero(b), numero(c));
  if (id === 8) return entero(a) % 2 === 0;
  if (id >= 9 && id <= 12) {
    const cuentas = vocales(String(a));
    return id === 9
      ? cuentas.a
      : id === 10
        ? Object.keys(cuentas)
            .filter((v) => cuentas[v])
            .join(" ")
        : id === 11
          ? Object.values(cuentas).reduce((s, n) => s + n, 0)
          : cuentas;
  }
  if ([13, 14].includes(id)) {
    const lista = [2, 3, 5, 7].filter((d) => entero(a) % d === 0);
    return id === 13 ? lista.length > 0 : lista;
  }
  if (id === 15) return divisores(a);
  if (id === 16) {
    const otros = divisores(b);
    return divisores(a).filter((d) => otros.includes(d));
  }
  if (id === 17) return esPrimo(a);
  if (id === 18) {
    if (numero(a) < 0) throw new RangeError("Edad no negativa");
    return a > 18;
  }
  if (id === 19) return calificacion(a);
  if (id === 20) return a.join("-");
  if (id === 21) {
    let suma = 0;
    const errores = [];
    for (const valor of a) {
      const n =
        typeof valor === "number"
          ? valor
          : typeof valor === "string" && valor.trim() !== ""
            ? Number(valor)
            : NaN;
      if (Number.isFinite(n)) suma += n;
      else errores.push(valor);
    }
    return { suma, errores };
  }
  if (id === 22) return letraDni(a);
  if (id === 23) return piramide(30);
  if (id === 24) return piramide(a, { inversa: true });
  if (id === 25) return piramide(a, { acumulativa: true });
  if (id === 26) return multiplosHasta();
  throw new RangeError("Ejercicio entre 1 y 26");
}

/** Las entradas canceladas devuelven null: no se confunden con cero o texto. */
export function leerHastaCancelar(pedir = prompt) {
  const valores = [];
  for (
    let dato = pedir("Ingresá un valor; Cancelar termina");
    dato !== null;
    dato = pedir("Otro valor; Cancelar termina")
  )
    valores.push(dato);
  return valores;
}
