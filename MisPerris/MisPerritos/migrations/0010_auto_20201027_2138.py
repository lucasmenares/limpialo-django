# Generated by Django 2.2.16 on 2020-10-27 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MisPerritos', '0009_nosotros'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderGalery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=15)),
                ('text', models.CharField(max_length=65)),
                ('image', models.ImageField(upload_to='car')),
            ],
        ),
        migrations.DeleteModel(
            name='SliderGaleria',
        ),
        migrations.RenameField(
            model_name='sliderphoto',
            old_name='name',
            new_name='title',
        ),
    ]
