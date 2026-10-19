from rest_framework import serializers
from .models import Categoria, Producto, Variante

class VarianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variante
        fields = ['id', 'talla', 'color', 'stock', 'imagen']

class ProductoSerializer(serializers.ModelSerializer):
    categoria_nombre = serializers.CharField(source='categoria.nombre', read_only=True)
    variantes = VarianteSerializer(many=True, read_only=True)

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'descripcion', 'precio', 'imagen', 'categoria', 'categoria_nombre', 'activo', 'variantes']

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ['id', 'nombre']
