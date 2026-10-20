import test from "node:test";
import assert from "node:assert/strict";
import { readdir, readFile, stat } from "node:fs/promises";
import { resolve, dirname, extname } from "node:path";
import { fileURLToPath } from "node:url";
import { productos } from "../../Web/Trabajos-Practicos/Cocina/recursos/productos.js";

const raiz = resolve(dirname(fileURLToPath(import.meta.url)), "../..");
test("cada plato tiene una ilustración local propia", async () => {
  assert.equal(new Set(productos.map((p) => p.imagen)).size, productos.length);
  for (const producto of productos) {
    const destino = resolve(
      raiz,
      "Web/Trabajos-Practicos/Cocina/11-SPA",
      producto.imagen,
    );
    assert.ok((await stat(destino)).isFile());
  }
});
async function archivos(carpeta) {
  const salida = [];
  for (const entrada of await readdir(carpeta, { withFileTypes: true })) {
    const ruta = resolve(carpeta, entrada.name);
    if (entrada.isDirectory()) salida.push(...(await archivos(ruta)));
    else salida.push(ruta);
  }
  return salida;
}
test("páginas de JavaScript y Cocina: enlaces y recursos locales presentes", async () => {
  const paginas = [
    ...(await archivos(resolve(raiz, "JavaScript"))),
    ...(await archivos(resolve(raiz, "Web/Trabajos-Practicos/Cocina"))),
  ].filter((p) => extname(p) === ".html");
  for (const pagina of paginas) {
    const html = await readFile(pagina, "utf8");
    assert.match(html, /<html lang="es">/);
    assert.match(html, /<meta\s+name="viewport"/);
    for (const coincidencia of html.matchAll(
      /(?<![:\w-])(?:src|href)="([^"{}]+)"/g,
    )) {
      const recurso = coincidencia[1];
      if (recurso.startsWith("#") || /^[a-z]+:/i.test(recurso)) continue;
      const destino = resolve(dirname(pagina), recurso.split(/[?#]/)[0]);
      assert.ok(
        (await stat(destino)).isFile() || (await stat(destino)).isDirectory(),
        `${pagina}: ${recurso}`,
      );
    }
    assert.doesNotMatch(
      html,
      /(?:src|href)="https?:\/\//,
      "Las actividades no necesitan CDN",
    );
  }
});
test("licencias y bibliotecas de la cursada incluidas", async () => {
  for (const nombre of [
    "bootstrap.min.css",
    "bootstrap.bundle.min.js",
    "jquery.min.js",
    "vue.min.js",
    "LICENSE-bootstrap.txt",
    "LICENSE-jquery.txt",
    "LICENSE-vue.txt",
    "LICENSE-popper.md",
  ]) {
    assert.ok(
      (await stat(resolve(raiz, "Web/recursos/vendor", nombre))).size > 0,
    );
  }
});
