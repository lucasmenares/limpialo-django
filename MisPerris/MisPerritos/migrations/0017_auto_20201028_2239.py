# Generated by Django 2.2.16 on 2020-10-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisPerritos', '0016_auto_20201028_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumo',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='insumo',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
