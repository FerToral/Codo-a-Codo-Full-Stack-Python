from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.test import TestCase, Client
from .models import Articulo, Cliente, Post, Categoria


class RecorridoCompleto(TestCase):
    def test_articulos_consulta_y_demo_idempotente(self):
        call_command("cargar_demo", verbosity=0)
        call_command("cargar_demo", verbosity=0)
        self.assertEqual(Articulo.objects.count(), 3)
        self.assertEqual(
            self.client.get("/tienda/?prd=tabla").context["articulos"].count(), 1
        )
        self.assertContains(self.client.get("/tienda/?prd=ausente"), "No hay artículos")
        self.assertContains(self.client.get("/tienda/?prd=" + "x" * 21), "hasta veinte")
        self.assertEqual(self.client.get("/tienda/").status_code, 200)

    def test_contacto_validacion_escape_y_csrf(self):
        self.assertContains(self.client.get("/contacto/"), "csrfmiddlewaretoken")
        invalido = self.client.post(
            "/contacto/", {"asunto": "Prueba", "email": "incorrecto", "mensaje": "Hola"}
        )
        self.assertTrue(invalido.context["form"].errors)
        valido = self.client.post(
            "/contacto/",
            {
                "asunto": "<script>alert(1)</script>",
                "email": "demo@example.test",
                "mensaje": "Prueba",
            },
        )
        self.assertContains(valido, "&lt;script&gt;")
        self.assertNotContains(valido, "<script>")
        self.assertEqual(
            Client(enforce_csrf_checks=True).post("/contacto/", {}).status_code, 403
        )

    def test_edades_con_contexto_historico(self):
        self.assertContains(self.client.get("/fundamentos/edades/60/2029/"), "69 años")
        self.assertEqual(
            self.client.get("/fundamentos/edades/1/2010/").status_code, 400
        )

    def test_modelos_y_baja_de_autor(self):
        cliente = Cliente.objects.create(
            nombre="Demo",
            email="demo@example.test",
            edad=20,
            direccion="Dirección ficticia",
            telefono="000",
        )
        self.assertEqual(cliente.telefono, "000")
        autor = get_user_model().objects.create_user(username="ejemplo", password=None)
        post = Post.objects.create(titulo="Prueba", contenido="Demo", autor=autor)
        categoria = Categoria.objects.create(nombre="Ejemplo")
        post.categorias.add(categoria)
        autor.delete()
        self.assertEqual(Post.objects.count(), 0)
        self.assertEqual(Categoria.objects.count(), 1)
