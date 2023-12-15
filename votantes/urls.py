from django.urls import path
from . import views

urlpatterns = [
    path('registrar/', views.registrar_votante, name='votante_registrar'),
    path('listar/', views.listar_votantes, name='votante_listar'),
    path('editar/<int:pk>/', views.editar_votante, name='votante_editar'),
    path('eliminar/<int:pk>/', views.eliminar_votante, name='votante_eliminar'),

    path('cantiad_votantes_lider/<int:lider_id>/',
         views.cantidad_votantes_lider, name='cantiad_votantes_lider'),
    path('cantidad_votates_total/', views.cantidad_total_votantes,
         name='cantidad_votantes_total'),
    path('cantidad_votantes_municipio/<int:municipio_id>/',
         views.cantidad_votantes_municipio, name='cantidad_votantes_municipio'),
    path('cantidad_votantes_mesas/<int:mesa_id>/',
         views.cantidad_votantes_mesa, name='cantidad_votantes_mesas'),
]
