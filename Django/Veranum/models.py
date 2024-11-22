from django.db import models
from django.contrib.auth.models import User

# Modelo para Clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Reservas
class ReservaHora(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.CharField(max_length=100)
    fecha = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return f"Reserva de {self.cliente} para {self.servicio} el {self.fecha} a las {self.hora}"

# Modelo para Habitaciones
class Habitacion(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

# Modelo para Proveedores
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField()
    rubro = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

# Modelo para Facturas
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Factura #{self.id} - Cliente: {self.cliente}"

# Modelo para Empleados
class Empleado(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para Servicios
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# Modelo para Órdenes de Pedido
class OrdenPedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    productos = models.TextField()  # Lista de productos solicitados
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Orden #{self.id} - Proveedor: {self.proveedor}"

# Modelo para Recepción de Productos
class RecepcionProducto(models.Model):
    orden_pedido = models.ForeignKey(OrdenPedido, on_delete=models.CASCADE)
    fecha_recepcion = models.DateField(auto_now_add=True)
    productos_recibidos = models.TextField()

    def __str__(self):
        return f"Recepción #{self.id} - Orden: {self.orden_pedido}"
