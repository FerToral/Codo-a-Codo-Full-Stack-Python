# Codo a Codo · Full Stack Python

Prácticas y proyectos de la formación Full Stack de Codo a Codo: desde páginas con HTML y CSS hasta aplicaciones con JavaScript, Vue, bases de datos y Django.

## Recorrido

| Área                                                   | Prácticas                                                                   |
| ------------------------------------------------------ | --------------------------------------------------------------------------- |
| [HTML y CSS](Web/Trabajos-Practicos/Astronomia/)       | Órbita: seis páginas, navegación, tablas y formulario                       |
| [Bootstrap, DOM y Vue](Web/Trabajos-Practicos/Cocina/) | La cocina de Juan: diseño adaptable, catálogo, datos reactivos y SPA        |
| [JavaScript](JavaScript/)                              | Fundamentos, funciones, arrays, cadenas, eventos y almacenamiento local     |
| [Bases de datos](Bases-de-Datos/)                      | 60 actividades SQL y 35 de empleados y departamentos, con datos de práctica |
| [Python](Python/)                                      | Fundamentos, colecciones, control de flujo, excepciones, funciones y POO    |
| [Django](Django/ProyectoWeb/)                          | Vistas, ORM, formularios, pedidos, servicios, blog y administración         |

Cada módulo incluye instrucciones y material de trabajo. El [mapa de la cursada](docs/material-de-la-cursada.md) relaciona conceptos y actividades; el [recorrido web](docs/trabajos-practicos-web.md) sigue la evolución de los trabajos.

## Empezar por la web

Desde la raíz del repositorio:

```console
python -m http.server 8000 --bind 127.0.0.1
```

Abrir:

- `http://127.0.0.1:8000/Web/Trabajos-Practicos/Astronomia/`
- `http://127.0.0.1:8000/Web/Trabajos-Practicos/Cocina/07-Bootstrap/`
- `http://127.0.0.1:8000/JavaScript/`

Las bibliotecas y los recursos visuales están incluidos. Los formularios estáticos validan localmente, sin enviar datos.

## Python

| Módulo                                                  | Contenido                                                 |
| ------------------------------------------------------- | --------------------------------------------------------- |
| [Guía U1](Python/00-guia-practica-u1/)                  | Expresiones, decisiones, entrada/salida y ciclos          |
| [Funciones](Python/01-funciones/)                       | Parámetros y valores de retorno                           |
| [Colecciones](Python/02-colecciones/)                   | Listas, tuplas y diccionarios                             |
| [Condicionales](Python/03-condicionales/)               | Selección, máximos, calculadora y media                   |
| [Bucles y generadores](Python/04-bucles-y-generadores/) | Acumulación, búsqueda y yield                             |
| [Excepciones](Python/05-excepciones/)                   | Conversión de entradas y raíz cuadrada                    |
| [POO · Banco](Python/06-poo/Banco/)                     | Abstracción, herencia, polimorfismo y gestión de clientes |
| [Guía U2](Python/07-guia-practica-u2/)                  | 38 actividades de funciones, fechas, números y cadenas    |

Con Python 3.10 o posterior:

```console
python Python/03-condicionales/calculadora.py
python Python/06-poo/Banco/banco.py
python Python/07-guia-practica-u2/consola.py --help
python -m unittest discover -s pruebas -v
```

## Aplicación Django

El [proyecto web](Django/ProyectoWeb/) tiene su entorno y dependencias separados. Su README explica cómo crear la base, cargar datos ficticios y comenzar con el administrador. Requiere Python 3.12 y Django 5.2.

## Comprobaciones web

Con Node.js 20 o posterior, sin instalar paquetes:

```console
npm run test:web
node JavaScript/demostracion.mjs
```

## Créditos

Autor: Fernando Toralez. Se incluyen prácticas históricas y desarrollos posteriores sobre las consignas de la cursada. El material de terceros y las bibliotecas conservan sus [créditos y licencias](CREDITOS.md).
