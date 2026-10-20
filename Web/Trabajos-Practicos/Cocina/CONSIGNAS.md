# Trabajos prácticos 07 a 11

## TP07 · Bootstrap

Construir una página adaptable con menú de navegación, botón de menú en pantallas pequeñas, carrusel y una zona de tres columnas. En escritorio las columnas quedan una al lado de otra; en tablet la columna derecha pasa debajo; en teléfono se apilan las tres. Esta práctica usa los cortes de 576 y 765 píxeles indicados en el trabajo.

Comprobar el menú con teclado y el carrusel con sus controles. Las diapositivas no avanzan automáticamente, para permitir leer el contenido sin apuro.

## TP08 · Plantillas con JavaScript

Guardar la cabecera y el pie en variables utilizando template strings. Insertarlos en elementos identificados mediante `id` y reutilizar el archivo en las páginas de inicio, nosotros y contacto. Marcar la página actual en el menú.

## TP09 · Array de productos

Definir objetos con código, imagen, nombre y descripción. Recorrer el array para generar el catálogo. Los datos se encuentran en `recursos/productos.js`; los elementos se crean en `08-09-DOM/catalogo.js`. El filtro agrega una aplicación práctica de cadenas y eventos. La plantilla compartida usa HTML estático de confianza; el catálogo inserta texto con `textContent`.

## TP10 · Vue básico

Incorporar Vue al menos en una página del sitio. Declarar el array en `data`, representar productos con `v-for` y organizar las tarjetas con Bootstrap. Aplicar `v-model` y una propiedad calculada para filtrar sin modificar el array original.

## TP11 · Single Page Application

Construir el sitio dentro de un único documento HTML. Cambiar las secciones con Vue sin recargar, mantener la búsqueda y la categoría al navegar, y permitir enlaces directos a cada sección. La implementación usa rutas de fragmento (`#carta`, por ejemplo), una lista de rutas admitidas y actualización del foco al cambiar de sección.

## Conceptos para repasar

- Bootstrap aporta estilos y componentes; JavaScript conecta datos, eventos y DOM.
- Una plantilla compartida evita duplicar el menú en cada archivo.
- Vue vincula estado e interfaz: no hace falta reconstruir manualmente toda la página.
- Validar en el cliente mejora la interacción, pero no reemplaza la validación del servidor.
- Una SPA no exige un servicio externo para funcionar en este ejercicio.

Referencia académica: trabajos TP07–TP11 de Codo a Codo, Full Stack Python, material compartido de 2020. La numeración se conserva para seguir la secuencia de clase.
