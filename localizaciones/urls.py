from django.urls import path
from . import views

urlpatterns = [
    path('departamentos/', views.departamento_list, name='departamento-list'),
    path('departamentos/<int:pk>/', views.departamento_detail,
         name='departamento-detail'),
    path('departamentos/create/', views.departamento_create,
         name='departamento-create'),
    path('departamentos/update/<int:pk>/',
         views.departamento_update, name='departamento-update'),
    path('departamentos/delete/<int:pk>/',
         views.departamento_delete, name='departamento-delete'),

    path('municipios/', views.municipio_list, name='municipio-list'),
    path('municipios/<int:pk>/', views.municipio_detail, name='municipio-detail'),
    path('municipios/create/', views.municipio_create, name='municipio-create'),
    path('municipios/update/<int:pk>/',
         views.municipio_update, name='municipio-update'),
    path('municipios/delete/<int:pk>/',
         views.municipio_delete, name='municipio-delete'),

    path('barrios/', views.barrio_list, name='barrio-list'),
    path('barrios/<int:pk>/', views.barrio_detail, name='barrio-detail'),
    path('barrios/create/', views.barrio_create, name='barrio-create'),
    path('barrios/update/<int:pk>/', views.barrio_update, name='barrio-update'),
    path('barrios/delete/<int:pk>/', views.barrio_delete, name='barrio-delete'),

    path('comunas/', views.comuna_list, name='comuna-list'),
    path('comunas/<int:pk>/', views.comuna_detail, name='comuna-detail'),
    path('comunas/create/', views.comuna_create, name='comuna-create'),
    path('comunas/update/<int:pk>/', views.comuna_update, name='comuna-update'),
    path('comunas/delete/<int:pk>/', views.comuna_delete, name='comuna-delete'),

    path('puestos/', views.puesto_list, name='puesto-list'),
    path('puestos/<int:pk>/', views.puesto_detail, name='puesto-detail'),
    path('puestos/create/', views.puesto_create, name='puesto-create'),
    path('puestos/update/<int:pk>/', views.puesto_update, name='puesto-update'),
    path('puestos/delete/<int:pk>/', views.puesto_delete, name='puesto-delete'),
]
