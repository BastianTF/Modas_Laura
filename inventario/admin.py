# Register your models here.

from django.contrib import admin
from .models import Categoria, Producto, Variante

class VarianteInline(admin.TabularInline):
    model = Variante
    extra = 1 # Te da espacio para añadir variantes rápidamente

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'categoria', 'precio', 'activo')
    list_filter = ('categoria', 'activo')
    search_fields = ('nombre', 'descripcion')
    inlines = [VarianteInline]

admin.site.register(Categoria)
