from django.contrib import admin
from webapp.models import Album, Photo, Favorites

# Register your models here.

class AlbumAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at', 'private']
    list_filter = ['name', 'description']
    search_fields = ['name','description']
    fields = ['id', 'name', 'description', 'created_at', 'private', 'author']
    readonly_fields = ['id', 'created_at']

class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'signature', 'created_at', 'private']
    list_filter = ['signature', 'created_at']
    search_fields = ['signature','private']
    fields = ['id', 'photo', 'signature', 'created_at', 'private', 'album', 'author']
    readonly_fields = ['id', 'created_at']

class FavoritesAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'user']
    list_filter = ['photo', 'user']
    search_fields = ['photo']
    fields = ['id', 'photo', 'user']
    readonly_fields = ['id']





admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Favorites, FavoritesAdmin)