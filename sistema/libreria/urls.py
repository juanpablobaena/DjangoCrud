from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static


urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('libros', views.libros, name='libros'),
    path('libros/crearLibro', views.crearLibro, name='crearLibro'),
    path('eliminarLibro/<int:id>', views.eliminar, name='eliminarLibro'),
    path('libros/editar/<int:id>', views.editar, name='editar')

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)