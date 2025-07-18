# Generated by Django 5.2.1 on 2025-05-25 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("App_LUMINOVA", "0003_fabricante_alter_ordenproduccion_notas"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ordenventa",
            name="estado",
            field=models.CharField(
                choices=[
                    ("PENDIENTE", "Pendiente Confirmación"),
                    ("INSUMOS_SOLICITADOS", "Insumos Solicitados"),
                    ("CONFIRMADA", "Confirmada (Esperando Producción)"),
                    ("PRODUCCION_INICIADA", "Producción Iniciada"),
                    ("PRODUCCION_CON_PROBLEMAS", "Producción con Problemas"),
                    ("LISTA_ENTREGA", "Lista para Entrega"),
                    ("COMPLETADA", "Completada/Entregada"),
                    ("CANCELADA", "Cancelada"),
                ],
                default="PENDIENTE",
                max_length=50,
            ),
        ),
    ]
