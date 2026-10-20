import test from "node:test";
import assert from "node:assert/strict";
import {
  actividades,
  resolver,
  letraDni,
  divisores,
  esPrimo,
  leerHastaCancelar,
} from "../01-fundamentos/ejercicios.js";
import * as f from "../02-funciones/ejercicios.js";
import * as a from "../03-arrays-y-cadenas/ejercicios.js";
import {
  productos,
  filtrarProductos,
} from "../../Web/Trabajos-Practicos/Cocina/recursos/productos.js";

test("los 26 ejercicios aceptan sus ejemplos", () => {
  assert.equal(actividades.length, 26);
  actividades.forEach(([, datos], i) =>
    assert.doesNotThrow(() => resolver(i + 1, datos)),
  );
  assert.equal(resolver(5, [3, 5]), 8);
  assert.equal(resolver(9, ["La casa"]), 3);
  assert.deepEqual(resolver(14, [30]), [2, 3, 5]);
  assert.deepEqual(resolver(16, [12, 18]), [1, 2, 3, 6]);
  assert.equal(resolver(18, [18]), false);
  assert.equal(resolver(19, [10]), "Sobresaliente");
  assert.deepEqual(resolver(21, [[2, "3", "", null, "error"]]), {
    suma: 5,
    errores: ["", null, "error"],
  });
  assert.deepEqual(resolver(24, [3]), ["333", "22", "1"]);
  assert.deepEqual(resolver(25, [3]), ["1", "12", "123"]);
  assert.equal(resolver(26).length, 600);
});
test("divisores, primos, DNI y entradas canceladas", () => {
  assert.deepEqual(divisores(-9), [1, 3, 9]);
  assert.throws(() => divisores(0));
  assert.equal(esPrimo(1), false);
  assert.equal(esPrimo(97), true);
  assert.equal(esPrimo(100), false);
  assert.equal(letraDni(0), "T");
  assert.equal(letraDni(12345678), "Z");
  assert.throws(() => letraDni(100000000));
  const entradas = ["", 0, "texto", null];
  assert.deepEqual(
    leerHastaCancelar(() => entradas.shift()),
    ["", 0, "texto"],
  );
  assert.throws(() => resolver(5, ["3", 2]));
  assert.throws(() => resolver(19, [11]));
});
test("funciones y geometría", () => {
  assert.equal(f.maximo(-2, -3), -2);
  assert.equal(f.promedio3(6, 8, 10), 8);
  assert.equal(f.promedioNotas([]), null);
  assert.equal(f.promedioNotas([6, 8, 10]), 8);
  assert.deepEqual(f.imprimirValores(3), {
    siguiente: 4,
    doble: 6,
    cuadrado: 9,
  });
  assert.equal(f.dobleDelSiguiente(3), 8);
  assert.equal(f.dobleDelSiguienteAlCuadrado(3), 64);
  assert.equal(f.perimetroCuadrado(4), 16);
  assert.equal(f.superficieCuadrado(4), 16);
  assert.equal(f.circunferencia(2), 4 * Math.PI);
  assert.equal(f.areaCirculo(2), 4 * Math.PI);
  assert.throws(() => f.areaCirculo(-1));
});
test("arrays sin ordenar ni modificar la entrada", () => {
  const valores = Object.freeze([
    3, 6, 67, 6, 23, 11, 100, 8, 93, 0, 17, 24, 7, 1, 33, 45, 28, 33, 23, 12,
    99, 100,
  ]);
  assert.equal(a.minimo(valores), 0);
  assert.equal(a.maximo(valores), 100);
  assert.equal(a.enPosicion(valores, 2), 6);
  assert.throws(() => a.enPosicion(valores, 0));
  assert.deepEqual(a.repetidos(valores), [6, 23, 100, 33]);
  assert.deepEqual(a.recorrerWhile([18, 21]), [18, 21]);
  assert.deepEqual(a.paresFor([18, 21, 30]), [18, 30]);
  assert.throws(() => a.minimo([]));
  assert.equal(a.unir(["Red", "Green"]), "Red, Green");
});
test("cadenas y números invertidos", () => {
  assert.equal(a.invertirNumero(32443), 34423);
  assert.equal(a.invertirNumero(-120), -21);
  assert.equal(a.alfabetico("webmaster"), "abeemrstw");
  assert.equal(a.titulo("curso de javascript"), "Curso De Javascript");
  assert.equal(a.palabraMasLarga("Curso de desarrollo web"), "desarrollo");
  assert.equal(a.palabraMasLarga("uno dos"), "uno");
});
test("catálogo: datos completos y filtros sin alterar productos", () => {
  assert.equal(new Set(productos.map((p) => p.codigo)).size, productos.length);
  productos.forEach((p) =>
    ["codigo", "imagen", "nombre", "descripcion"].forEach((k) =>
      assert.ok(p[k]),
    ),
  );
  assert.equal(filtrarProductos(productos, "CALABAZA", "Vegano").length, 2);
  assert.equal(filtrarProductos(productos, "no existe").length, 0);
  assert.equal(productos.length, 6);
});
