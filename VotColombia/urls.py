from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('usuarios.urls')),
    path('ubicacion/', include('localizaciones.urls')),
    path('votantes/', include('votantes.urls')),
]
