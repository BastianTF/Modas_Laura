from django.test import TestCase
from rest_framework.test import APIClient

from .models import Categoria, Producto, Variante


class CatalogoApiTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.categoria = Categoria.objects.create(nombre='Vestidos')
        self.producto = Producto.objects.create(
            nombre='Vestido floral',
            descripcion='Vestido de verano',
            categoria=self.categoria,
            precio=25000,
            activo=True,
        )
        Variante.objects.create(
            producto=self.producto,
            talla='M',
            color='Azul',
            stock=3,
        )

    def test_lista_categorias(self):
        response = self.client.get('/api/categorias/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [{'id': self.categoria.id, 'nombre': 'Vestidos'}])

    def test_lista_productos_incluye_variantes(self):
        Producto.objects.create(
            nombre='Producto inactivo',
            categoria=self.categoria,
            precio=10000,
            activo=False,
        )

        response = self.client.get('/api/productos/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], 'Vestido floral')
        self.assertEqual(response.data[0]['categoria_nombre'], 'Vestidos')
        self.assertEqual(
            response.data[0]['variantes'],
            [{
                'id': self.producto.variantes.get().id,
                'talla': 'M',
                'color': 'Azul',
                'stock': 3,
                'imagen': None,
            }],
        )
