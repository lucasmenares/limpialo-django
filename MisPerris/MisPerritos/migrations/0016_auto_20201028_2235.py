# Generated by Django 2.2.16 on 2020-10-28 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisPerritos', '0015_insumo_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='price',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='stock',
            field=models.TextField(),
        ),
    ]
