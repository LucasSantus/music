from django.contrib import admin
from django.urls import path, include
from musica.api import MusicaViewSet
from rest_framework_nested import routers
from musica.views import index
from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

api_router = routers.DefaultRouter()
api_router.register(r"music", MusicaViewSet)

channels_router = routers.NestedDefaultRouter(api_router, r"music", lookup="musicas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(api_router.urls)),   
    path("api/", include(channels_router.urls)),
    path("", index, name="index"),

    # caminho para servir arquivos
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
]
