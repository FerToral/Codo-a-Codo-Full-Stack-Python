from datetime import date
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.db import transaction
from aula.models import Cliente, Pedido, Servicio, Categoria, Post


class Command(BaseCommand):
    help = "Carga datos ficticios sin crear credenciales de acceso. Se puede repetir."

    @transaction.atomic
    def handle(self, *args, **options):
        cliente, _ = Cliente.objects.get_or_create(
            email="alex@example.test", defaults={"nombre": "Alex Ejemplo", "edad": 25}
        )
        Pedido.objects.get_or_create(
            numero=1001, defaults={"cliente": cliente, "fecha": date(2020, 11, 20)}
        )
        for titulo, contenido in [
            (
                "Diseño web",
                "Páginas adaptables con estructura semántica y navegación clara.",
            ),
            (
                "Desarrollo de aplicaciones",
                "Datos, formularios y reglas del negocio conectados con Django.",
            ),
            (
                "Mantenimiento",
                "Revisión de contenido y pequeñas mejoras sobre una aplicación existente.",
            ),
        ]:
            Servicio.objects.get_or_create(
                titulo=titulo, defaults={"contenido": contenido}
            )
        autor, creado = get_user_model().objects.get_or_create(
            username="autor_demo",
            defaults={
                "first_name": "Equipo",
                "last_name": "de práctica",
                "is_active": False,
            },
        )
        if creado:
            autor.set_unusable_password()
            autor.save()
        categoria, _ = Categoria.objects.get_or_create(nombre="Desarrollo web")
        post, _ = Post.objects.get_or_create(
            titulo="De la vista a la plantilla",
            autor=autor,
            defaults={
                "contenido": "Una vista prepara los datos y la plantilla define su presentación. La herencia de plantillas permite compartir navegación y estilos sin repetir todo el documento."
            },
        )
        post.categorias.add(categoria)
        self.stdout.write(
            self.style.SUCCESS(
                "Datos de práctica disponibles. Para acceder a gestión, creá tu superusuario."
            )
        )
