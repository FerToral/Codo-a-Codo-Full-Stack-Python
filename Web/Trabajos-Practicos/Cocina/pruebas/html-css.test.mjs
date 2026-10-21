import { test } from "node:test";
import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import vm from "node:vm";
import { fileURLToPath } from "node:url";
const root = path.resolve(
  path.dirname(fileURLToPath(import.meta.url)),
  "../01-06-HTML-CSS",
);
const pages = [
  "index.html",
  "receta.html",
  "nosotros.html",
  "registro.html",
  "sucursales.html",
  "clientes.html",
];

test("HTML/CSS: seis páginas semánticas con navegación y recursos locales", () => {
  for (const page of pages) {
    const html = fs.readFileSync(path.join(root, page), "utf8");
    assert.match(html, /<html lang="es">/);
    assert.match(html, /<main id="contenido">/);
    assert.equal((html.match(/aria-current="page"/g) || []).length, 1);
    assert.equal((html.match(/<h1>/g) || []).length, 1);
    for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
      const url = match[1];
      if (/^(?:https?:|#|data:)/.test(url)) continue;
      assert.ok(
        fs.existsSync(path.resolve(root, url.split("#")[0])),
        page + ": " + url,
      );
    }
  }
});
test("HTML/CSS: tablas, listas, iconos, iframe, galería y tipografía incluidos", () => {
  const receta = fs.readFileSync(path.join(root, "receta.html"), "utf8");
  assert.match(receta, /<caption>/);
  assert.match(receta, /<ol>/);
  assert.match(receta, /scope="col"/);
  const sedes = fs.readFileSync(path.join(root, "sucursales.html"), "utf8");
  assert.match(sedes, /<iframe[^>]+title="[^"]+"[^>]+loading="lazy"/);
  assert.match(sedes, /target="mapa-sedes"/);
  const galeria = fs.readFileSync(path.join(root, "clientes.html"), "utf8");
  assert.equal((galeria.match(/<figure>/g) || []).length, 6);
  assert.equal((galeria.match(/<img[^>]+alt="[^"]+"/g) || []).length, 6);
  const css = fs.readFileSync(path.join(root, "cocina.css"), "utf8");
  for (const n of [1100, 760, 420])
    assert.match(css, new RegExp("max-width:\\s*" + n + "px"));
  assert.match(css, /@font-face/);
  assert.match(css, /prefers-reduced-motion/);
  assert.match(css, /@keyframes/);
  assert.match(css, /display:\s*grid/);
});
function simular(valido) {
  const elementos = [],
    estado = { textContent: "" },
    resumen = { hidden: true };
  const clave = { value: "ficticia-de-prueba" };
  let listener,
    enfocado = false,
    reportado = false;
  const formulario = {
    elements: { clave },
    addEventListener: (_, fn) => (listener = fn),
    checkValidity: () => valido,
    reportValidity: () => (reportado = true),
  };
  const contenedor = {
    replaceChildren: () => (elementos.length = 0),
    append: (...xs) => elementos.push(...xs),
  };
  const payload = "<img src=x onerror=alert(1)>";
  const contexto = {
    document: {
      querySelector: (s) =>
        ({
          "#registro": formulario,
          "#estado": estado,
          "#resumen": resumen,
          "#datos-resumen": contenedor,
          "#titulo-resumen": { focus: () => (enfocado = true) },
        })[s],
      createElement: (tag) => ({ tag, textContent: "" }),
    },
    FormData: class {
      *[Symbol.iterator]() {
        yield ["nombre", payload];
        yield ["clave", clave.value];
      }
    },
  };
  const script = fs.readFileSync(path.join(root, "formulario.js"), "utf8");
  assert.doesNotMatch(
    script,
    /innerHTML|fetch\(|localStorage|sessionStorage|location\./,
  );
  vm.runInNewContext(script, contexto);
  let prevenido = false;
  listener({ preventDefault: () => (prevenido = true) });
  return {
    elementos,
    estado,
    resumen,
    clave,
    enfocado,
    reportado,
    payload,
    prevenido,
  };
}
test("formulario: previsualización como texto, sin clave, envío ni almacenamiento", () => {
  const s = simular(true);
  assert.equal(s.elementos[1].textContent, s.payload);
  assert.equal(s.elementos.length, 2);
  assert.equal(s.clave.value, "");
  assert.equal(s.resumen.hidden, false);
  assert.equal(s.enfocado, true);
  assert.equal(s.prevenido, true);
  assert.match(s.estado.textContent, /No se enviaron ni guardaron/);
});
test("formulario: entrada inválida no crea resumen", () => {
  const s = simular(false);
  assert.equal(s.reportado, true);
  assert.equal(s.resumen.hidden, true);
  assert.equal(s.elementos.length, 0);
});
