
from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect









# Modelo personalizado para usuarios
class Usuario(AbstractUser):
    ROLES = (
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
        ('empleado', 'Empleado'),
    )
    rol = models.CharField(max_length=20, choices=ROLES)
    telefono = models.CharField(max_length=15, blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='veranum_usuario_groups',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='veranum_usuario_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

# Modelo Cliente
class Cliente(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='cliente')
    direccion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.usuario.username


# Modelo Empleado
class Empleado(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empleado')
    cargo = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario.username

# Modelo Proveedor
class Proveedor(models.Model):
    nombre = models.CharField(max_length=255)
    contacto = models.CharField(max_length=255)
    rubro = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

# Modelo Producto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
=======
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
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

<<<<<<< HEAD
# Modelo Orden de Pedido
class OrdenPedido(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ManyToManyField(Producto)
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Orden #{self.id} - {self.proveedor.nombre}"

# Modelo Servicio
class Servicio(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

# Modelo Reserva de hora
class ReservaHora(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=50, default='Pendiente')

    def __str__(self):
        return f"Reserva #{self.id} - {self.cliente.usuario.username}"

# Modelo Factura/Boleta
class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicios = models.ManyToManyField(Servicio)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, default='Emitida')

    def __str__(self):
        return f"Factura #{self.id} - {self.cliente.usuario.username}"
    
class RecepcionProducto(models.Model):
    orden_pedido = models.ForeignKey(OrdenPedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    estado = models.CharField(max_length=50, default='Pendiente')
    fecha_recepcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recepción #{self.id} - {self.producto.nombre}"    

class CustomLoginView(LoginView):
    template_name = 'inicio.html'

    def form_valid(self, form):
        return redirect('dash')
=======
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
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b
