from django.db import models
import uuid


class Concessionaria(models.Model):
    SETOR_CHOICES = [
        ('oficina', 'Oficina'), ('showroom', 'Showroom'),
    ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        null=False,
        blank=True
    )

    codigo = models.CharField(
        max_length=8,
        null=False,
        blank=False
    )

    setor = models.CharField(
        max_length=30,
        null=False,
        blank=False,
        choices=SETOR_CHOICES
    )

    veiculo = models.DecimalField(
        max_digits=5,
        null=False,
        blank=False,
        decimal_places=2
    )

    quantidade_veiculos = models.IntegerField(
        max_length=5,
        null=False,
        blank=False,
    )
