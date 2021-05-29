from django.views.generic import View, TemplateView, RedirectView, FormView, ListView, CreateView, DetailView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from webapp.forms import AlbumForm, PhotoForm, SearchForm
from webapp.models import Album
from django.db.models import Q
from django.utils.http import urlencode
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied

class AlbumList(ListView):
    template_name = 'album/list.html'
    model = Album
    context_object_name = 'albums'
    ordering = ('-created_at',)

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(AlbumList, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            queryset = queryset.filter(author=self.request.user, private='private')
        else:
            queryset = queryset.filter(private='public')

        if self.search_data:
            queryset = queryset.filter(
                Q(name__icontains=self.search_data) |
                Q(description__icontains=self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})

        return context


class AlbumCreate(CreateView):
    template_name = 'album/create.html'
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('webapp:home')

    def form_valid(self, form):
        user = self.request.user
        album = form.save(commit=False)
        album.author = user
        album.save()
        return redirect('webapp:home')

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        return super().dispatch(request, *args, **kwargs)


class AlbumEdit(UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'album/edit.html'
    context_object_name = 'album'
    success_url = reverse_lazy('webapp:home')

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        if not user.has_perm('webapp.change_album'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class AlbumDelete(DeleteView):
    model = Album
    template_name = 'album/delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('webapp:home')


    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('accounts:login')
        if not user.has_perm('webapp.delete_album'):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class AlbumView(DetailView):
    model = Album
    template_name = 'album/view.html'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect('webapp:home')
        return super().dispatch(request, *args, **kwargs)

