# Generated by Django 3.1.2 on 2020-11-19 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animes', '0003_auto_20201119_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='imagen_descripcion',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='imagen_logo',
            field=models.ImageField(default=1, upload_to='img'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='imagen_portada',
            field=models.ImageField(default=2, upload_to='img'),
            preserve_default=False,
        ),
    ]
