from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_votante, name='votante_registrar'),
]
