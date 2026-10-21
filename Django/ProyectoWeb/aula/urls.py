from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("fundamentos/saludo/", views.saludo, name="saludo"),
    path("fundamentos/fecha/", views.fecha, name="fecha"),
    path("fundamentos/plantilla/", views.plantilla, name="plantilla"),
    path("fundamentos/edades/<int:edad>/<int:anio>/", views.edad, name="edad"),
    path("tienda/", views.tienda, name="tienda"),
    path("contacto/", views.contacto, name="contacto"),
    path("servicios/", views.servicios, name="servicios"),
    path("blog/", views.blog, name="blog"),
    path("pedidos/", views.pedidos, name="pedidos"),
    path("clientes/nuevo/", views.editar, {"tipo": "cliente"}, name="cliente_nuevo"),
    path(
        "clientes/<int:pk>/editar/",
        views.editar,
        {"tipo": "cliente"},
        name="cliente_editar",
    ),
    path(
        "clientes/<int:pk>/eliminar/",
        views.eliminar,
        {"tipo": "cliente"},
        name="cliente_eliminar",
    ),
    path("pedidos/nuevo/", views.editar, {"tipo": "pedido"}, name="pedido_nuevo"),
    path(
        "pedidos/<int:pk>/editar/",
        views.editar,
        {"tipo": "pedido"},
        name="pedido_editar",
    ),
    path(
        "pedidos/<int:pk>/eliminar/",
        views.eliminar,
        {"tipo": "pedido"},
        name="pedido_eliminar",
    ),
]
