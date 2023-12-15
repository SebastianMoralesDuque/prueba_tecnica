from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/login/', TokenObtainPairView.as_view(),
         name='admin_token_obtain_pair'),
    path('admin/refresh/', TokenRefreshView.as_view(), name='admin_token_refresh'),

    path('lider/login/', views.lider_login, name='lider-login'),
    path('lider/refresh/', TokenRefreshView.as_view(),
         name='leader_token_refresh'),

    path('lider/registrar/', views.registrar_lider, name='leader_registrar'),

    path('capitan/', views.listar_capitanes, name='capitan-list'),
    path('capitan/crear/', views.crear_capitan, name='capitan-crear'),
    path('capitan/editar/<int:pk>/',
         views.actualizar_capitan, name='capitan-editar'),
    path('capitan/eliminar/<int:pk>/',
         views.eliminar_capitan, name='capitan-eliminar'),
]
