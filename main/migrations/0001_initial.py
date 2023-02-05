# Generated by Django 4.1.6 on 2023-02-05 21:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concessionaria',
            fields=[
                ('id', models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=8)),
                ('setor', models.CharField(choices=[('oficina', 'Oficina'), ('showroom', 'Showroom')], max_length=30)),
                ('veiculo', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantidade_veiculos', models.IntegerField(max_length=5)),
            ],
        ),
    ]
