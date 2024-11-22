from django.contrib import admin
<<<<<<< HEAD



# Register your models here.

=======
from .models import (
    Cliente,
    ReservaHora,
    Habitacion,
    Proveedor,
    Factura,
    Empleado,
    Servicio,
    OrdenPedido,
    RecepcionProducto,
)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'email', 'telefono')
    search_fields = ('nombre', 'apellido', 'email')
    list_filter = ('apellido',)

@admin.register(ReservaHora)
class ReservaHoraAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servicio', 'fecha', 'hora')
    search_fields = ('cliente__nombre', 'servicio')
    list_filter = ('fecha',)

@admin.register(Habitacion)
class HabitacionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'disponible')
    search_fields = ('nombre',)
    list_filter = ('disponible',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contacto', 'telefono', 'email', 'rubro')
    search_fields = ('nombre', 'rubro')
    list_filter = ('rubro',)

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'total')
    search_fields = ('cliente__nombre',)
    list_filter = ('fecha',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'nombre', 'apellido', 'cargo')
    search_fields = ('nombre', 'apellido', 'usuario__username')
    list_filter = ('cargo',)

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    search_fields = ('nombre',)
    list_filter = ('precio',)

@admin.register(OrdenPedido)
class OrdenPedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'fecha', 'total')
    search_fields = ('proveedor__nombre',)
    list_filter = ('fecha',)

@admin.register(RecepcionProducto)
class RecepcionProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'orden_pedido', 'fecha_recepcion')
    search_fields = ('orden_pedido__proveedor__nombre',)
    list_filter = ('fecha_recepcion',)
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b
