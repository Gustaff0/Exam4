from django.urls import path
from webapp.views import AlbumList, AlbumDelete, AlbumEdit, AlbumView, AlbumCreate, PhotoCreate, PhotoEdit, PhotoView, PhotoDelete

app_name = 'webapp'

urlpatterns = [
    path('', AlbumList.as_view(), name='home'),
    path('delete_album/<int:pk>/', AlbumDelete.as_view(), name='album_delete'),
    path('create_album/', AlbumCreate.as_view(), name='album_create'),
    path('view_album/<int:pk>/', AlbumView.as_view(), name='album_view'),
    path('edit_album/<int:pk>/', AlbumEdit.as_view(), name='album_edit'),
    path('create_photo/<int:pk>/', PhotoCreate.as_view(), name='photo_create'),
    path('edit_photo/<int:pk>/', PhotoEdit.as_view(), name='photo_edit'),
    path('delete_photo/<int:pk>', PhotoDelete.as_view(), name='photo_delete'),
    path('view_photo/<int:pk>', PhotoView.as_view(), name='photo_view')
]