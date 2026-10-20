from datetime import date
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Q
from django.db.models.deletion import ProtectedError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .forms import ClienteForm, PedidoForm
from .models import Cliente, Pedido, Servicio, Post, Categoria


def inicio(request):
    return render(request, "inicio.html", {"servicios": Servicio.objects.all()[:3]})


def saludo(request):
    return HttpResponse("Hola mundo", content_type="text/plain; charset=utf-8")


def fecha(request):
    return HttpResponse(
        timezone.localdate().isoformat(), content_type="text/plain; charset=utf-8"
    )


def plantilla(request):
    persona = {
        "nombre": "Alex",
        "apellido": "Ejemplo",
        "edad": 18,
        "hermanos": ["Sol", "Leo"],
    }
    return render(
        request, "fundamentos.html", {"persona": persona, "hoy": date.today()}
    )


def servicios(request):
    return render(request, "servicios.html", {"servicios": Servicio.objects.all()})


def blog(request):
    publicaciones = Post.objects.select_related("autor").prefetch_related("categorias")
    categoria = None
    if request.GET.get("categoria"):
        from django.http import Http404

        try:
            identificador = int(request.GET["categoria"])
        except (ValueError, TypeError):
            raise Http404("Categoría inexistente")
        categoria = get_object_or_404(Categoria, pk=identificador)
        publicaciones = publicaciones.filter(categorias=categoria)
    return render(
        request,
        "blog.html",
        {
            "publicaciones": publicaciones,
            "categorias": Categoria.objects.all(),
            "categoria": categoria,
        },
    )


@staff_member_required
def pedidos(request):
    consulta = request.GET.get("q", "").strip()[:100]
    listado = Pedido.objects.select_related("cliente")
    if consulta:
        listado = listado.filter(
            Q(cliente__nombre__icontains=consulta)
            | Q(cliente__email__icontains=consulta)
        )
    return render(
        request,
        "pedidos.html",
        {"pedidos": listado, "clientes": Cliente.objects.all(), "consulta": consulta},
    )


@staff_member_required
@require_http_methods(["GET", "POST"])
def editar(request, tipo, pk=None):
    modelo, formulario, etiqueta = (
        (Cliente, ClienteForm, "cliente")
        if tipo == "cliente"
        else (Pedido, PedidoForm, "pedido")
    )
    instancia = get_object_or_404(modelo, pk=pk) if pk else None
    form = formulario(
        request.POST if request.method == "POST" else None, instance=instancia
    )
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, f"Se guardó el {etiqueta}.")
        return redirect("pedidos")
    return render(
        request,
        "formulario.html",
        {"form": form, "titulo": f"{'Editar' if pk else 'Nuevo'} {etiqueta}"},
    )


@staff_member_required
@require_http_methods(["GET", "POST"])
def eliminar(request, tipo, pk):
    modelo = Cliente if tipo == "cliente" else Pedido
    objeto = get_object_or_404(modelo, pk=pk)
    if request.method == "POST":
        try:
            objeto.delete()
        except ProtectedError:
            messages.error(
                request,
                "El cliente tiene pedidos asociados. Primero revisá esos pedidos.",
            )
        else:
            messages.success(request, "Se eliminó el registro.")
        return redirect("pedidos")
    return render(request, "eliminar.html", {"objeto": objeto})
