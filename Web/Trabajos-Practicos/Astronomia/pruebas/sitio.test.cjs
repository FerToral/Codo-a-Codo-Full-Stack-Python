const { test } = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const root = path.resolve(__dirname, "..");
const pages = [
  "index.html",
  "pag0.html",
  "pag1.html",
  "pag2.html",
  "pag3.html",
  "pag4.html",
];
test("contenido principal sin recursos remotos ni citas extensas heredadas", () => {
  for (const page of pages) {
    const html = fs.readFileSync(path.join(root, page), "utf8");
    assert.doesNotMatch(
      html,
      /<(?:img|iframe|script|link)[^>]+(?:src|href)="https?:/,
    );
    assert.doesNotMatch(
      html,
      /Mira ese punto|todos los que amas|taringa|fontawesome|fonts.googleapis/i,
    );
    assert.match(html, /<svg[^>]+role="img"/);
  }
});
for (const page of pages)
  test(page + ": idioma, navegación y recursos locales", () => {
    const html = fs.readFileSync(path.join(root, page), "utf8");
    assert.match(html, /<html lang="es">/);
    assert.equal((html.match(/aria-current="page"/g) || []).length, 1);
    assert.match(
      html,
      new RegExp(
        'href="' +
          page.replace(".", "\\.") +
          '"\\s+class="active"\\s+aria-current="page"',
      ),
    );
    assert.match(html, /src="sitio.js"/);
    assert.equal(
      (html.match(/<script\b/g) || []).length,
      (html.match(/<\/script>/g) || []).length,
    );
    for (const match of html.matchAll(/(?:src|href)="([^"]+)"/g)) {
      const url = match[1];
      if (/^(?:https?:|data:|#)/.test(url)) continue;
      assert.ok(
        fs.existsSync(path.join(root, url.split("#")[0])),
        "recurso " + url,
      );
    }
    assert.doesNotMatch(html, /<script[^>]+src="https?:/);
  });
test("contacto tiene campos asociados y no pide contraseña ni cuenta ficticia", () => {
  const html = fs.readFileSync(path.join(root, "pag4.html"), "utf8");
  for (const id of ["nombre", "correo", "mensaje"])
    assert.match(html, new RegExp('for="' + id + '"'));
  assert.match(html, /<form\s+id="contacto"[^>]+method="dialog"/);
  assert.match(html, /<textarea[^>]+name="mensaje"[^>]+required/);
  assert.doesNotMatch(html, /type="password"/);
  assert.match(html, /<title>Contacto/);
});
test("todos los iframes explican su contenido y son diferidos", () => {
  for (const page of pages) {
    const html = fs.readFileSync(path.join(root, page), "utf8");
    for (const frame of html.matchAll(/<iframe\b([^>]*)>/g)) {
      assert.match(frame[1], /title="Recurso audiovisual de /);
      assert.match(frame[1], /loading="lazy"/);
    }
  }
});
function simulate(valid, exists = true) {
  const state = {
    prevented: false,
    reported: false,
    text: "",
    fetches: 0,
    stores: 0,
  };
  let listener;
  const form = {
    addEventListener: (_, fn) => (listener = fn),
    checkValidity: () => valid,
    reportValidity: () => (state.reported = true),
  };
  const status = {
    set textContent(v) {
      state.text = v;
    },
  };
  vm.runInNewContext(fs.readFileSync(path.join(root, "sitio.js"), "utf8"), {
    document: {
      querySelector: (s) =>
        s === "#contacto" ? (exists ? form : null) : status,
    },
    fetch: () => {
      state.fetches++;
    },
    localStorage: { setItem: () => state.stores++ },
  });
  if (listener) listener({ preventDefault: () => (state.prevented = true) });
  return state;
}
test("formulario válido informa sin transmitir ni persistir", () => {
  const state = simulate(true);
  assert.equal(state.prevented, true);
  assert.match(state.text, /no se enviaron ni guardaron/);
  assert.equal(state.fetches, 0);
  assert.equal(state.stores, 0);
});
test("formulario inválido informa y muestra validación", () => {
  const state = simulate(false);
  assert.equal(state.reported, true);
  assert.match(state.text, /Revisá/);
  assert.equal(state.prevented, true);
  assert.equal(state.fetches, 0);
});
test("páginas sin formulario no provocan errores de script", () =>
  assert.doesNotThrow(() => simulate(true, false)));
test("estilos cubren tres puntos de corte y movimiento reducido", () => {
  const css = fs.readFileSync(path.join(root, "astronomia.css"), "utf8");
  for (const width of [1023, 640, 380])
    assert.match(css, new RegExp("max-width:\\s*" + width + "px"));
  assert.match(css, /prefers-reduced-motion/);
  assert.match(css, /grid-template/);
  assert.match(css, /focus-visible/);
});
