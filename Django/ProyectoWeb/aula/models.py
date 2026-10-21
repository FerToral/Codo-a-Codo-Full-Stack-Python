from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    edad = models.PositiveSmallIntegerField(validators=[MaxValueValidator(120)])
    direccion = models.CharField(max_length=150, blank=True)
    telefono = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ["nombre", "pk"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(edad__lte=120), name="edad_hasta_120"
            )
        ]

    def __str__(self):
        return self.nombre


class Pedido(models.Model):
    numero = models.PositiveIntegerField(unique=True, validators=[MinValueValidator(1)])
    cliente = models.ForeignKey(
        Cliente, on_delete=models.PROTECT, related_name="pedidos"
    )
    fecha = models.DateField()
    entregado = models.BooleanField(default=False)

    class Meta:
        ordering = ["-fecha", "-numero"]
        constraints = [
            models.CheckConstraint(
                condition=models.Q(numero__gte=1), name="numero_positivo"
            )
        ]

    def __str__(self):
        return f"Pedido {self.numero}"


class Articulo(models.Model):
    nombre = models.CharField(max_length=80)
    seccion = models.CharField(max_length=60)
    precio = models.PositiveIntegerField()

    class Meta:
        ordering = ["nombre", "pk"]

    def __str__(self):
        return f"{self.nombre} · {self.seccion} · {self.precio}"


class Servicio(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="servicios/", blank=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["titulo"]

    def __str__(self):
        return self.titulo


class Categoria(models.Model):
    nombre = models.CharField(max_length=60, unique=True)
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre


class Post(models.Model):
    titulo = models.CharField(max_length=150)
    contenido = models.TextField()
    imagen = models.ImageField(upload_to="blog/", blank=True)
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="publicaciones"
    )
    categorias = models.ManyToManyField(Categoria, related_name="publicaciones")
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-creado", "-pk"]

    def __str__(self):
        return self.titulo
