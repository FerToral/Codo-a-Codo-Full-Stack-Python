# JavaScript

Ejercicios de fundamentos, funciones, arrays, cadenas y manipulación del DOM. El recorrido termina en las prácticas web de la cocina, donde los objetos, las plantillas y los eventos se aplican a un sitio.

| Carpeta               | Contenido                                                         |
| --------------------- | ----------------------------------------------------------------- |
| `01-fundamentos`      | 26 ejercicios de expresiones, decisiones y ciclos                 |
| `02-funciones`        | Composición, promedios y geometría                                |
| `03-arrays-y-cadenas` | 11 actividades sin ordenar el array de entrada                    |
| `04-dom-y-eventos`    | Formulario, creación de elementos, eventos y almacenamiento local |

## Usar las prácticas

Desde la raíz del repositorio:

```console
python -m http.server 8000 --bind 127.0.0.1
node JavaScript/demostracion.mjs
npm run test:web
```

Abrir `http://127.0.0.1:8000/JavaScript/`. El selector de ejercicios permite cambiar los argumentos y ver el resultado. La página de diálogos muestra `alert`, `prompt` y cancelación; `document.write` se aísla en un iframe para no reemplazar la página de trabajo.

En la práctica DOM se pueden agregar, marcar y quitar tareas. Sólo la preferencia de tema se guarda en `localStorage`; la lista se reinicia al recargar. Los textos del usuario se insertan como texto, no como HTML.

Las [consignas](CONSIGNAS.md) conservan la numeración de las actividades de clase. Los módulos exportan funciones para poder probar la lógica sin depender del navegador.
