from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
choices = [('private', 'Private'), ('public', 'Public')]

class Album(models.Model):
    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.CharField(max_length=1000, null=True, blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author_album',  verbose_name='АвторАльбома')
    created_at = models.DateTimeField(auto_now_add=True)
    private = models.CharField(max_length=200, choices=choices, null=False, blank=False, default='public')


class Photo(models.Model):
    photo = models.ImageField(null=False, blank=False, upload_to='gallery_pics', verbose_name='Картинка')
    signature = models.CharField(max_length=1000, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='author',  verbose_name='Автор')
    album = models.ForeignKey('webapp.Album', on_delete=models.CASCADE, related_name='album', verbose_name='Альбом')
    private = models.CharField(max_length=200, choices=choices, null=False, blank=False, default='public')


class Favorites(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user', verbose_name='Пользователь')
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE, related_name='photo_f', verbose_name='Фото')



