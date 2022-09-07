from django.contrib import admin
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import ListaViewSet, MercadoViewSet, ProdutoViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'listas', ListaViewSet)
router.register(r'mercados', MercadoViewSet)
router.register(r'produtos', ProdutoViewSet)
router.register(r'usuarios', UsuarioViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]