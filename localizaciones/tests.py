from django.test import TestCase
from .models import Municipio
from localizaciones.models import Departamento


class MunicipioTestCase(TestCase):
    def setUp(self):
        departamento = Departamento.objects.create(nombre="Departamento 1")

        Municipio.objects.create(
            nombre="Municipio 1",
            departamento=departamento
        )

    def test_municipio_creado_correctamente(self):
        municipio = Municipio.objects.get(nombre="Municipio 1")
        self.assertEqual(municipio.nombre, "Municipio 1")

    def test_municipio_no_vacio(self):
        municipios = Municipio.objects.all()
        self.assertTrue(municipios.exists())
