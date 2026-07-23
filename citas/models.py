from django.db import models


# Create your models here.
class Barbero(models.Model):
    nombre_barbero = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_barbero


# Base de datos para los tipos de servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.ImageField(upload_to="servicios/", blank=True, null=True)

    def __str__(self):
        return self.nombre


class Cita(models.Model):

    class Estado(models.TextChoices):
        CONFIRMADA = "CONFIRMADA", "Confirmada"
        CANCELADA = "CANCELADA", "Cancelada"
        FINALIZADA = "FINALIZADA", "Finalizada"

    nombre_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    barbero = models.ForeignKey(
        Barbero,
        on_delete=models.CASCADE,
        related_name="reservas",
        null=True,
        blank=True
    )
    servicio = models.ForeignKey(
        Servicio,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=Estado.choices,
        default=Estado.CONFIRMADA
    )
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["fecha", "hora"]
        unique_together = ["barbero", "fecha", "hora"]

    def __str__(self):
        return f"{self.nombre_cliente} - {self.fecha} {self.hora}"
