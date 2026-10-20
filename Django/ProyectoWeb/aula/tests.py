from io import StringIO
from django.contrib.auth import get_user_model
from django.core.management import call_command
from django.db.models.deletion import ProtectedError
from django.test import Client, TestCase
from django.urls import reverse
from .forms import ClienteForm, PedidoForm
from .models import Cliente, Pedido, Servicio, Post


class ProyectoWebTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        call_command("cargar_demo", stdout=StringIO())
        cls.usuario = get_user_model().objects.create_user("operador", is_staff=True)

    def test_paginas_y_plantillas(self):
        for nombre in ["inicio", "saludo", "fecha", "plantilla", "servicios", "blog"]:
            with self.subTest(nombre=nombre):
                self.assertEqual(self.client.get(reverse(nombre)).status_code, 200)
        self.assertContains(self.client.get(reverse("plantilla")), "Alex")
        self.assertContains(
            self.client.get(reverse("blog")), "De la vista a la plantilla"
        )

    def test_carga_repetible_y_autor_sin_acceso(self):
        call_command("cargar_demo", stdout=StringIO())
        self.assertEqual(Cliente.objects.count(), 1)
        self.assertEqual(Pedido.objects.count(), 1)
        self.assertEqual(Servicio.objects.count(), 3)
        self.assertEqual(Post.objects.count(), 1)
        autor = get_user_model().objects.get(username="autor_demo")
        self.assertFalse(autor.has_usable_password())
        self.assertFalse(autor.is_active)

    def test_gestion_requiere_acceso(self):
        self.assertRedirects(
            self.client.get(reverse("pedidos")),
            "/admin/login/?next=/pedidos/",
            fetch_redirect_response=False,
        )
        self.assertEqual(
            self.client.post(reverse("cliente_nuevo"), {}).status_code, 302
        )

    def test_alta_edicion_y_baja(self):
        self.client.force_login(self.usuario)
        response = self.client.post(
            reverse("cliente_nuevo"),
            {"nombre": "Sol", "email": "sol@example.test", "edad": 30},
        )
        self.assertRedirects(response, reverse("pedidos"))
        cliente = Cliente.objects.get(email="sol@example.test")
        self.client.post(
            reverse("cliente_editar", args=[cliente.pk]),
            {"nombre": "Sol Modelo", "email": cliente.email, "edad": 31},
        )
        cliente.refresh_from_db()
        self.assertEqual(cliente.nombre, "Sol Modelo")
        response = self.client.post(
            reverse("pedido_nuevo"),
            {"numero": 1002, "cliente": cliente.pk, "fecha": "2020-11-21"},
        )
        self.assertRedirects(response, reverse("pedidos"))
        pedido = Pedido.objects.get(numero=1002)
        self.client.get(reverse("pedido_eliminar", args=[pedido.pk]))
        self.assertTrue(Pedido.objects.filter(pk=pedido.pk).exists())
        self.client.post(reverse("pedido_eliminar", args=[pedido.pk]))
        self.client.post(reverse("cliente_eliminar", args=[cliente.pk]))
        self.assertFalse(Cliente.objects.filter(pk=cliente.pk).exists())

    def test_integridad_y_validacion(self):
        cliente = Cliente.objects.first()
        with self.assertRaises(ProtectedError):
            cliente.delete()
        self.assertFalse(
            ClienteForm({"nombre": " ", "email": "incorrecto", "edad": 121}).is_valid()
        )
        self.assertFalse(
            PedidoForm(
                {"numero": 0, "cliente": cliente.pk, "fecha": "2020-11-20"}
            ).is_valid()
        )
        self.assertFalse(
            PedidoForm(
                {"numero": 1001, "cliente": cliente.pk, "fecha": "2020-11-20"}
            ).is_valid()
        )
        self.client.force_login(self.usuario)
        response = self.client.post(
            reverse("cliente_eliminar", args=[cliente.pk]), follow=True
        )
        self.assertContains(response, "tiene pedidos asociados")

    def test_csrf_y_escape(self):
        seguro = Client(enforce_csrf_checks=True)
        seguro.force_login(self.usuario)
        self.assertEqual(seguro.post(reverse("cliente_nuevo"), {}).status_code, 403)
        self.client.force_login(self.usuario)
        cliente = Cliente.objects.first()
        cliente.nombre = '<script>alert("x")</script>'
        cliente.save()
        pagina = self.client.get(reverse("pedidos"))
        self.assertContains(pagina, "&lt;script&gt;")
        self.assertNotContains(pagina, '<script>alert("x")</script>')

    def test_filtro_de_blog_y_busqueda(self):
        post = Post.objects.first()
        categoria = post.categorias.first()
        self.assertContains(
            self.client.get(reverse("blog"), {"categoria": categoria.pk}), post.titulo
        )
        self.assertEqual(
            self.client.get(reverse("blog"), {"categoria": 999}).status_code, 404
        )
        self.client.force_login(self.usuario)
        self.assertContains(
            self.client.get(reverse("pedidos"), {"q": "no-existe"}), "No hay pedidos"
        )

    def test_admin_y_formularios(self):
        self.usuario.is_superuser = True
        self.usuario.save()
        self.client.force_login(self.usuario)
        for ruta in [
            "/admin/",
            "/admin/aula/servicio/add/",
            "/admin/aula/post/add/",
            "/clientes/nuevo/",
            "/pedidos/nuevo/",
        ]:
            with self.subTest(ruta=ruta):
                self.assertEqual(self.client.get(ruta).status_code, 200)
