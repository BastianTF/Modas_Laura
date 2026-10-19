# Create your models here.

from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre de la Categoría")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=200, verbose_name="Nombre del Producto")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos', verbose_name="Categoría")
    precio = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Precio (CLP)") # Sin decimales para Pesos Chilenos
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True, verbose_name="Foto del Producto")
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True, verbose_name="Disponible para la venta")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return self.nombre


class Variante(models.Model):
    """
    Este modelo permite controlar el inventario real. 
    Evita que vendas una prenda si no queda stock de esa talla o color específico.
    """
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='variantes')
    talla = models.CharField(max_length=10, verbose_name="Talla (ej: S, M, L, 42, 4)")
    color = models.CharField(max_length=50, verbose_name="Color")
    stock = models.PositiveIntegerField(default=0, verbose_name="Cantidad en Inventario")
    imagen = models.ImageField(upload_to='productos/variantes/', blank=True, null=True, verbose_name="Foto de este color")

    class Meta:
        verbose_name = "Variante de Producto"
        verbose_name_plural = "Variantes de Productos"
        # Evita duplicar la misma combinación de talla y color para el mismo producto
        unique_together = ('producto', 'talla', 'color')

    def __str__(self):
        return f"{self.producto.nombre} - {self.talla} / {self.color} (Stock: {self.stock})"
