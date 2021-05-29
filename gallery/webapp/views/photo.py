from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import AlbumForm, PhotoForm, SearchForm
from webapp.models import Album, Photo
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

class PhotoCreate(CreateView):
    template_name = 'photo/create.html'
    form_class = PhotoForm
    model = Photo

    def get_success_url(self):
        return reverse(
            'webapp:album_view',
            kwargs={'pk': self.kwargs.get('pk')}
        )

    def form_valid(self, form):
        album = get_object_or_404(Album, id=self.kwargs.get('pk'))
        photo = form.save(commit=False)
        photo.album = album
        photo.author = self.request.user
        photo.save()
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        if not user.has_perm('webapp.create_photo'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class PhotoDelete(DeleteView):
    model = Photo

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('webapp:album_view', kwargs={'pk': self.object.album.pk})

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        if not user.has_perm('webapp.delete_photo'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class PhotoEdit(UpdateView):
    model = Photo
    template_name = 'photo/edit.html'
    form_class = PhotoForm
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('webapp:photo_view', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        if not user.has_perm('webapp.change_photo'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)



class PhotoView(DetailView):
    model = Photo
    template_name = 'photo/view.html'


