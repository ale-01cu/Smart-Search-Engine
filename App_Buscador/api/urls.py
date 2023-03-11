from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContenidoView, BusquedaView

router = DefaultRouter()
router.register('contenido/resultadoBusqueda', BusquedaView, basename='busqueda')
router.register('contenido', ContenidoView, basename='contenido')

urlpatterns = router.urls