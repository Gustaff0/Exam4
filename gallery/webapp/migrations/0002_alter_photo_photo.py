# Generated by Django 3.2.3 on 2021-05-29 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='gallery_pics', verbose_name='Картинка'),
        ),
    ]
