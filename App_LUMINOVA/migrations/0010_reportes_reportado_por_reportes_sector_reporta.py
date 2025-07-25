# Generated by Django 5.2.1 on 2025-05-29 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App_LUMINOVA", "0009_alter_insumo_cantidad_en_pedido"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="reportes",
            name="reportado_por",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reportes_creados",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="reportes",
            name="sector_reporta",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="reportes_originados_aqui",
                to="App_LUMINOVA.sectorasignado",
            ),
        ),
    ]
