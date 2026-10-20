# Órbita · Astronomía

Sitio de astronomía desarrollado como trabajo práctico de HTML y CSS de Codo a Codo. Se organiza en seis páginas: inicio, estrellas, astronomía, sistema solar, satélites y contacto.

## Qué se trabaja

Estructura semántica, navegación entre páginas, listas, tablas, imágenes SVG, diseño adaptable y validación de formularios. La identidad original de la entrega es TP N.º 2.

## Ejecutar

Abrir index.html o servir la carpeta:

```console
python -m http.server 8768 --bind 127.0.0.1
```

El contenido principal funciona sin conexión. Los textos y diagramas están incluidos; no se cargan fuentes, fotos ni bibliotecas remotas. Los diagramas no están a escala.

El formulario de contacto valida los campos y muestra un resultado local. No envía ni guarda información.

## Comprobar

```console
node --test pruebas/sitio.test.cjs
```

Las pruebas revisan navegación, recursos, formulario y estilos adaptables.

## Lecturas

- [NASA Science · Stars](https://science.nasa.gov/universe/stars/)
- [NASA Science · Solar System Facts](https://science.nasa.gov/solar-system/solar-system-facts/)
- [NASA Science · Moons](https://science.nasa.gov/solar-system/moons/)

Los textos breves y los diagramas del sitio son propios. Ver [créditos](../../../CREDITOS.md).
