# Proyecto web con Django

Práctica de vistas, plantillas, ORM, formularios y administración. La aplicación reúne los ejemplos de saludo y fecha, la gestión de clientes y pedidos, y un sitio con servicios y blog.

## Poner en marcha

Requiere Python 3.12 o posterior compatible con Django 5.2. Desde esta carpeta:

```console
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py cargar_demo
python manage.py createsuperuser
python manage.py runserver 127.0.0.1:8001
```

En Linux/macOS, activar con `source .venv/bin/activate`. Abrir `http://127.0.0.1:8001/`. El comando de demostración se puede repetir y no crea contraseñas. Para entrar a gestión o administración se usa el superusuario creado localmente.

## Recorrido

| Ruta | Conceptos |
| --- | --- |
| `/fundamentos/saludo/` y `/fundamentos/fecha/` | URL, vista y respuesta HTTP |
| `/fundamentos/plantilla/` | Contexto, variables, condiciones y ciclos |
| `/servicios/` | Consulta del ORM, imágenes y herencia de plantillas |
| `/blog/` | Autor, categorías, relación muchos a muchos y filtros |
| `/pedidos/` | Clientes, pedidos, formularios y operaciones de gestión |
| `/admin/` | Administración, búsqueda y carga de contenidos |

Las [actividades](ACTIVIDADES.md) siguen la secuencia de los ejemplos de Django del curso. SQLite permite comenzar sin configurar un servidor de base de datos; las prácticas de SQL están en el módulo correspondiente del repositorio.

## Archivos principales

- `aula/models.py`: entidades y relaciones.
- `aula/forms.py`: formularios y validaciones.
- `aula/views.py` y `urls.py`: solicitudes y navegación.
- `templates/`: base compartida y páginas del sitio.
- `static/`: estilos adaptables.
- `aula/management/commands/cargar_demo.py`: datos ficticios.

Para agregar imágenes a servicios o publicaciones, usar el administrador. Se guardan en `media/`, fuera de Git. Las imágenes son opcionales y no hacen falta para iniciar el proyecto.

## Comprobar

```console
python manage.py check
python manage.py test
python manage.py makemigrations --check --dry-run
```

Se verifican rutas, permisos, formularios, integridad de pedidos, datos de demostración, escape HTML y protección CSRF.

## Entorno local

Este proyecto está configurado para aprender con `DEBUG=1` y acceso por localhost. La clave de desarrollo se genera al iniciar el proceso; para conservar sesiones entre reinicios, definir `DJANGO_SECRET_KEY` en el entorno. No guardar claves en archivos versionados.

No publicar con `runserver`. Un despliegue requiere una clave estable, `DEBUG=0`, hosts explícitos, HTTPS, cookies seguras, gestión de archivos subidos y un servidor WSGI. La configuración falla si se desactiva DEBUG sin suministrar una clave.
