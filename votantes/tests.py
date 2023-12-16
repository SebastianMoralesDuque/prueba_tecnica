from localizaciones.models import Departamento, Municipio, Barrio, Comuna, PuestoVotacion
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from django.contrib.auth.models import User
from usuarios.models import Lider, UserProfile


class TestRegistrarLiderView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = User.objects.create_user(
            username='testuser', password='password')
        perfil_usuario = UserProfile.objects.create(
            user=self.usuario, is_lider=True)
        Lider.objects.create(user_profile=perfil_usuario, superusuario=self.usuario, nombres='Nombre',
                             apellidos='Apellido', ciudad='Ciudad', direccion='Dirección', foto_perfil='URL_de_la_imagen')
        self.login_url = 'http://127.0.0.1:8000/auth/lider/login/'

    def test_registrar_lider_sin_permisos(self):
        data = {
            "username": "lider",
            "nombres": "lider",
            "apellidos": "ApellidoPrueba",
            "ciudad": "CiudadPrueba",
            "direccion": "DireccionPrueba",
            "foto_perfil": "https://ejemplo.com/imagen.jpg",
            "password": "lider"
        }

        login_data = {'username': 'testuser', 'password': 'password'}
        response_login = self.client.post(
            self.login_url, login_data, format='json')

        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        access_token = response_login.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response_registrar = self.client.post(
            'http://127.0.0.1:8000/auth/lider/registrar/', data, format='json')

        self.assertEqual(response_registrar.status_code,
                         status.HTTP_403_FORBIDDEN)

    def test_registrar_lider_exitoso_como_admin(self):
        data = {
            "username": "lider",
            "nombres": "lider",
            "apellidos": "ApellidoPrueba",
            "ciudad": "CiudadPrueba",
            "direccion": "DireccionPrueba",
            "foto_perfil": "https://ejemplo.com/imagen.jpg",
            "password": "lider"
        }

        User.objects.create_superuser(
            'admin_username', 'admin@example.com', 'admin_password')
        admin_login_data = {'username': 'admin_username',
                            'password': 'admin_password'}
        admin_login_url = 'http://127.0.0.1:8000/auth/admin/login/'
        response_admin_login = self.client.post(
            admin_login_url, admin_login_data, format='json')

        self.assertEqual(response_admin_login.status_code, status.HTTP_200_OK)
        admin_access_token = response_admin_login.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + admin_access_token)
        response_registrar = self.client.post(
            'http://127.0.0.1:8000/auth/lider/registrar/', data, format='json')

        self.assertEqual(response_registrar.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(response_registrar.data.get(
            'message'), 'Líder registrado correctamente')
        self.assertIn('lider_id', response_registrar.data)

    def test_registrar_lider_con_datos_invalidos(self):
        data = {
            "username": "lider",
            "nombres": "lider",
            "apellidos": "ApellidoPrueba",
            "direccion": "DireccionPrueba",
            "foto_perfil": "https://ejemplo.com/imagen.jpg",
            "password": "lider"
        }
        User.objects.create_superuser(
            'admin_username', 'admin@example.com', 'admin_password')
        admin_login_data = {'username': 'admin_username',
                            'password': 'admin_password'}
        admin_login_url = 'http://127.0.0.1:8000/auth/admin/login/'
        response_admin_login = self.client.post(
            admin_login_url, admin_login_data, format='json')

        self.assertEqual(response_admin_login.status_code, status.HTTP_200_OK)
        admin_access_token = response_admin_login.data['access']

        self.client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + admin_access_token)
        response_registrar = self.client.post(
            'http://127.0.0.1:8000/auth/lider/registrar/', data, format='json')

        self.assertEqual(response_registrar.status_code,
                         status.HTTP_400_BAD_REQUEST)


class TestRegistrarVotanteView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.usuario = User.objects.create_user(
            username='testuser', password='password')
        self.perfil_usuario = UserProfile.objects.create(
            user=self.usuario, is_lider=True)
        self.lider = Lider.objects.create(user_profile=self.perfil_usuario, superusuario=self.usuario, nombres='Nombre',
                                          apellidos='Apellido', ciudad='Ciudad', direccion='Dirección', foto_perfil='URL_de_la_imagen')

        self.departamento = Departamento.objects.create(
            nombre='Departamento de Prueba')
        self.municipio = Municipio.objects.create(
            nombre='Municipio de Prueba', departamento=self.departamento)
        self.barrio = Barrio.objects.create(
            nombre='Barrio de Prueba', municipio=self.municipio)
        self.comuna = Comuna.objects.create(
            nombre='Comuna de Prueba', barrio=self.barrio)
        self.puesto_votacion = PuestoVotacion.objects.create(
            nombre='Puesto de Votación de Prueba', direccion='Dirección de Prueba', comuna=self.comuna)

        self.login_url = 'http://127.0.0.1:8000/auth/lider/login/'

    def test_registrar_votante_exitoso(self):
        login_data = {'username': 'testuser', 'password': 'password'}
        response_login = self.client.post(
            self.login_url, login_data, format='json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        access_token = response_login.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        data = {
            "nombres": "sebcas",
            "apellidos": "sebas",
            "direccion": "Calle Principal #123",
            "telefono": "1034518561",
            "cedula": "1004114468",
            "puesto_votacion": self.puesto_votacion.id_puesto_votacion
        }

        response_registrar = self.client.post(
            'http://127.0.0.1:8000/votantes/registrar/', data, format='json')

        self.assertEqual(response_registrar.status_code,
                         status.HTTP_201_CREATED)
        self.assertEqual(response_registrar.data.get(
            'message'), 'Votante registrado correctamente')

    def test_listar_votantes(self):
        login_data = {'username': 'testuser', 'password': 'password'}
        response_login = self.client.post(
            self.login_url, login_data, format='json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        access_token = response_login.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        response_listar = self.client.get(
            'http://127.0.0.1:8000/votantes/listar/', format='json')

        self.assertEqual(response_listar.status_code, status.HTTP_200_OK)

    def test_editar_votante(self):
        login_data = {'username': 'testuser', 'password': 'password'}
        response_login = self.client.post(
            self.login_url, login_data, format='json')
        self.assertEqual(response_login.status_code, status.HTTP_200_OK)
        access_token = response_login.data['access']

        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        data = {
            "nombres": "sebcas",
            "apellidos": "sebas",
            "direccion": "Calle Principal #123",
            "telefono": "1034518561",
            "cedula": "1004114468",
            "puesto_votacion": self.puesto_votacion.id_puesto_votacion
        }

        response_creacion = self.client.post(
            'http://127.0.0.1:8000/votantes/registrar/', data, format='json')

        self.assertEqual(response_creacion.status_code,
                         status.HTTP_201_CREATED)
        votante_id = response_creacion.data['id_votante']

        data_edicion = {
            "nombres": "editado",
            "apellidos": "editado",
            "direccion": "Calle Principal #123",
            "telefono": "1034518561",
            "cedula": "1004114468",
            "puesto_votacion": self.puesto_votacion.id_puesto_votacion
        }

        response_edicion = self.client.put(
            f'http://127.0.0.1:8000/votantes/editar/{votante_id}/', data_edicion, format='json')
        self.assertEqual(response_edicion.status_code, status.HTTP_200_OK)


def test_eliminar_votante(self):
    login_data = {'username': 'testuser', 'password': 'password'}
    response_login = self.client.post(
        self.login_url, login_data, format='json')
    self.assertEqual(response_login.status_code, status.HTTP_200_OK)
    access_token = response_login.data['access']

    self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

    data = {
        "nombres": "sebcas",
        "apellidos": "sebas",
        "direccion": "Calle Principal #123",
        "telefono": "1034518561",
        "cedula": "1004114468",
        "puesto_votacion": self.puesto_votacion.id_puesto_votacion
    }

    response_creacion = self.client.post(
        'http://127.0.0.1:8000/votantes/registrar/', data, format='json')

    self.assertEqual(response_creacion.status_code, status.HTTP_201_CREATED)

    votante_id = response_creacion.data['id_votante']

    response_eliminacion = self.client.delete(
        f'http://127.0.0.1:8000/votantes/eliminar/{votante_id}/')
    self.assertEqual(response_eliminacion.status_code,
                     status.HTTP_204_NO_CONTENT)
