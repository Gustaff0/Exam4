# Generated by Django 3.2.3 on 2021-05-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default=1, upload_to='gallery_pics', verbose_name='Картинка'),
            preserve_default=False,
        ),
    ]
