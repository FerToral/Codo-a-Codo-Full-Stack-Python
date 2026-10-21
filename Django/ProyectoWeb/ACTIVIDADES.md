# Django · de las vistas al sitio con datos

## 1. Primeras respuestas

Crear el proyecto, registrar una aplicación y conectar las URL con sus vistas. Devolver un saludo y la fecha del servidor como texto. Recibir un objeto persona en una plantilla y mostrar nombre, edad y una lista de hermanos mediante variables, condicionales y ciclos.

## 2. Modelos y ORM

Representar clientes con nombre, correo y edad, y pedidos con número, fecha y estado de entrega. Crear las migraciones y consultar los datos desde el ORM. En esta práctica cada pedido se relaciona con un cliente: no se puede borrar un cliente que tenga pedidos.

Realizar altas, búsquedas, cambios y bajas desde formularios. Rechazar correos inválidos, edades fuera de rango y números de pedido repetidos. Después de guardar, redirigir al listado para evitar repetir el POST al actualizar la página.

## 3. Plantillas y archivos estáticos

Compartir cabecera, navegación y pie con una plantilla base. Usar nombres de URL en los enlaces y cargar los estilos con la etiqueta `static`. Organizar inicio, servicios, blog y gestión como páginas del mismo sitio.

## 4. Servicios y administración

Crear un servicio con título, contenido, imagen y fechas automáticas. Registrarlo en administración y mostrar el listado en una plantilla. Configurar la carga de imágenes en desarrollo y presentar las fechas como campos de sólo lectura en el administrador.

## 5. Blog

Crear categorías y publicaciones. Cada publicación tiene título, contenido, imagen opcional, autor y varias categorías. Consultar los registros, mostrar el autor y las categorías, y filtrar por categoría. Usar `select_related` y `prefetch_related` para no generar una consulta por cada relación al recorrer la página.

## 6. Acceso y comprobaciones

Reservar clientes y pedidos para personal autorizado, conservar CSRF en los formularios y pedir confirmación antes de borrar. Crear datos ficticios sin contraseñas compartidas y comprobar que cargar la demostración dos veces no duplica registros.

## 7. Artículos, búsquedas y contacto

Crear Articulo con nombre,sección yprecio, registrar el modelo enadmin yconsultarlo por nombre usando icontains. La búsqueda admite hasta20caracteres einforma si no hay resultados. Completar dirección/teléfono delcliente yel borrado en cascada de publicaciones al eliminar alautor, como especifica la clase.

Crear el contacto mediante FormsAPI: asunto,email ymensaje. ValidarPOST,usar cleaned_data ymostrar confirmación con contenido escapado, sin guardar el mensaje ni inventar un envío de correo. Agregar el ejemplo de edad con parámetrosURL ybase2020 para conservar su contexto.

Configurar PostgreSQL con variables de entorno, conservandoSQLite como arranque rápido. Las credenciales no forman parte de una entrega pública.

## 8. Publicación

Distinguir archivos estáticos de archivos subidos, desarrollo de producción y alojamiento de servicio administrado. Antes de un despliegue real, revisar `check --deploy`, credenciales, hosts, HTTPS, copias de respaldo y permisos de los medios.

Material académico relacionado: ejemplos Proyecto2019 y TiendaEnLinea, y clase 38–39 de Django de Codo a Codo Full Stack. Estas actividades reúnen sus conceptos en una aplicación de práctica; los ejemplos y la teoría se conservan en el archivo de la cursada.
