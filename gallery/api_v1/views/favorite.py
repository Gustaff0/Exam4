from api_v1.serializers import FavoriteSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from rest_framework import generics
from webapp.models import Favorites
from rest_framework import viewsets


class Favorite(viewsets.ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoriteSerializer
