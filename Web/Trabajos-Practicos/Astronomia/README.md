# Órbita · práctica web de Codo a Codo

Sitio de astronomía de seis páginas, nacido como práctica HTML/CSS de
Fernando Toralez en 2020. El archivo histórico se identificaba como
Codo-a-Codo-TP-N-2; no se confunde con la trivia de Aprendé Programando
2019 ni con un proyecto final Django.

## Recorrido

Inicio → estrellas → astronomía → sistema solar → satélites → contacto.
Cada sección tiene navegación propia, jerarquía de lectura y referencias.
Las tablas, listas, enlaces y formularios conservan el enfoque de la práctica.

El nombre Órbita, la presentación adaptable, los textos y diagramas actuales
son mantenimiento de 2026. Los originales se preservan en el respaldo
histórico; no se atribuyen estas mejoras a la entrega de 2020.

## Ejecutar

Abrir index.html o servir esta carpeta:

    python -m http.server 8768 --bind 127.0.0.1

El contenido principal funciona sin conexión: no carga fotos, fuentes,
kits de iconos, iframes ni bibliotecas remotas. Los diagramas SVG se
dibujaron para este sitio y no están a escala. Los enlaces bibliográficos
requieren Internet.

El contacto sólo valida HTML y muestra un resultado local. No envía,
almacena ni solicita contraseñas. Para probarlo, usá datos ficticios.

## Consigna y autoría

La entrega personal conserva su identificación TP N.º 2. El índice de
la cursada relaciona las consignas TP01–TP11; no está acreditado que
el integrador TP06 sea la consigna exacta de este archivo. La revisión
no afirma cumplir todos esos TPs ni una evaluación docente. Los PDFs
relacionados permanecen vinculados en el respaldo privado.

Las fotografías remotas, citas extensas y recursos sin licencia acreditada
se sustituyeron en esta versión pública por redacción y gráficos nuevos.
No se publican los originales ajenos ni los PDFs docentes. Se conserva
la firma histórica de Fernando, sin atribuirle material de terceros.
Los iconos propios no se presentan como cumplimiento del requisito
FontAwesome de la consigna relacionada TP06.

## Lecturas

- [NASA Science · Stars](https://science.nasa.gov/universe/stars/)
- [NASA Science · Solar System Facts](https://science.nasa.gov/solar-system/solar-system-facts/)
- [NASA Science · Moons](https://science.nasa.gov/solar-system/moons/)
- [NASA · What is a satellite?](https://www.nasa.gov/general/what-is-a-satellite/)

Se consultaron para revisar conceptos; las explicaciones breves son
redacción nueva, no transcripciones ni imágenes tomadas de esas páginas.

## Verificación

    node --test pruebas/sitio.test.cjs

Navegación, recursos locales, formulario sin transmisión, ausencia de
dependencias remotas y estilos adaptables. La validación automática se
complementa con un recorrido real de la versión actual en navegador.
