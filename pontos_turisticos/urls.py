from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from core.api.viewsets import PontoTuristicoViewSet
from atracoes.api.viewsets import AtracoesViewset
from localizacao.api.viewsets import LocalizacaoViewset
from comentarios.api.viewsets import ComentariosViewset
from avaliacoes.api.viewsets import AvaliacoesViewset


router = routers.DefaultRouter()
router.register(r'pontoturistico', PontoTuristicoViewSet, basename='PontoTuristico')
router.register(r'atracoes', AtracoesViewset)
router.register(r'localizacao', LocalizacaoViewset)
router.register(r'comentarios', ComentariosViewset)
router.register(r'avaliacoes', AvaliacoesViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(router.urls)),
]
