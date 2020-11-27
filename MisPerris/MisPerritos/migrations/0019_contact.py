# Generated by Django 2.2.4 on 2020-11-27 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisPerritos', '0018_auto_20201028_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=120)),
                ('lastname', models.TextField(max_length=120)),
                ('subject', models.TextField(max_length=120)),
                ('ctype', models.IntegerField(choices=[(1, 'Solicitud'), (2, 'Reclamo'), (3, 'Sugerencia')], default=1)),
            ],
        ),
    ]