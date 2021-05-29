from django.urls import include, path
from rest_framework import routers
from api_v1 import views


router = routers.DefaultRouter()
router.register('favorite', views.Favorite)
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_v1'


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]