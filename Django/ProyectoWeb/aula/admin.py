from django.contrib import admin
from .models import Cliente, Pedido, Servicio, Categoria, Post


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ["nombre", "email", "edad"]
    search_fields = ["nombre", "email"]


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ["numero", "cliente", "fecha", "entregado"]
    list_filter = ["entregado", "fecha"]
    search_fields = ["cliente__nombre", "cliente__email"]


@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ["titulo", "creado", "actualizado"]
    readonly_fields = ["creado", "actualizado"]


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ["creado", "actualizado"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["titulo", "autor", "creado"]
    list_filter = ["categorias", "autor"]
    search_fields = ["titulo", "contenido"]
    readonly_fields = ["creado", "actualizado"]
    filter_horizontal = ["categorias"]
