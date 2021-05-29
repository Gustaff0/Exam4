from django.views.generic import DetailView, ListView, UpdateView
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.models import Album, Favorites


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = 'user_detail.html'
    context_object_name = 'user_obj'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['albums'] = Album.objects.filter(author=self.object.pk)
        context['favorites'] = Favorites.objects.filter(user=self.object.pk)
        return context
