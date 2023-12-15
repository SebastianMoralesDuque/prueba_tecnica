from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

from usuarios.models import Lider, UserProfile


class TestLogin(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = User.objects.create_user(
            username='testuser', password='password')
        perfil_usuario = UserProfile.objects.create(
            user=self.usuario, is_lider=True)
        Lider.objects.create(user_profile=perfil_usuario, superusuario=self.usuario, nombres='Nombre',
                             apellidos='Apellido', ciudad='Ciudad', direccion='Dirección', foto_perfil='URL_de_la_imagen')
        User.objects.create_superuser(
            'admin_username', 'admin@example.com', 'admin_password')

    def test_inicio_sesion_lider_exitoso(self):
        lider_login_data = {'username': 'testuser', 'password': 'password'}
        lider_login_url = 'http://127.0.0.1:8000/auth/lider/login/'
        response_lider_login = self.client.post(
            lider_login_url, lider_login_data, format='json')

        self.assertEqual(response_lider_login.status_code, status.HTTP_200_OK)
        self.assertIn('access', response_lider_login.data)

    def test_inicio_sesion_admin_exitoso(self):
        admin_login_data = {'username': 'admin_username',
                            'password': 'admin_password'}
        admin_login_url = 'http://127.0.0.1:8000/auth/admin/login/'
        response_admin_login = self.client.post(
            admin_login_url, admin_login_data, format='json')

        self.assertEqual(response_admin_login.status_code, status.HTTP_200_OK)
        self.assertIn('access', response_admin_login.data)
