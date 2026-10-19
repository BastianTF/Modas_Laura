from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Categoria, Producto
from .serializers import CategoriaSerializer, ProductoSerializer

class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):
    """Ofrece la lista de categorías a la web (Solo lectura para clientes)"""
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
    """Ofrece la lista de productos activos con sus tallas y colores a la web"""
    queryset = Producto.objects.filter(activo=True).order_by('-fecha_creacion')
    serializer_class = ProductoSerializer
