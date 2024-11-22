from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cliente, ReservaHora, Habitacion, Proveedor, Factura, Empleado, Servicio, OrdenPedido, RecepcionProducto
from .forms import ReservaHoraForm, HabitacionForm

# Página principal
def index(request):
    return render(request, 'pages/index.html')

# Vista para iniciar sesión
def login_view(request):
    return render(request, 'registration/login.html')

# Vista para cerrar sesión
def logout_view(request):
    return redirect('index')

# CRUD para Habitaciones
@login_required

def crud(request):
    return render(request, 'pages/crud.html')

def crud_habitacion(request):
    habitaciones = Habitacion.objects.all()
    return render(request, 'pages/crudhabitacion.html', {'habitaciones': habitaciones})

# Agregar una reserva
@login_required
def add_reserva(request):
    if request.method == 'POST':
        form = ReservaHoraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaHoraForm()
    return render(request, 'pages/add_reserva.html', {'form': form})

# Eliminar una reserva
@login_required
def delete_reserva(request, pk):
    reserva = get_object_or_404(ReservaHora, pk=pk)
    reserva.delete()
    return redirect('index')

# Actualizar una reserva
@login_required
def update_reserva(request, pk):
    reserva = get_object_or_404(ReservaHora, pk=pk)
    if request.method == 'POST':
        form = ReservaHoraForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ReservaHoraForm(instance=reserva)
    return render(request, 'pages/update_reserva.html', {'form': form})

# Registrar un cliente
@login_required
def registro_cliente(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
        return redirect('index')
    return render(request, 'pages/registro_cliente.html')

# Registrar una reserva de hora
@login_required
def registro_reserva_hora(request):
    reservas = ReservaHora.objects.all()
    return render(request, 'pages/registro_reserva_hora.html', {'reservas': reservas})

# Registrar un proveedor
@login_required
def registro_proveedor(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        contacto = request.POST.get('contacto')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        rubro = request.POST.get('rubro')
        Proveedor.objects.create(nombre=nombre, contacto=contacto, telefono=telefono, email=email, rubro=rubro)
        return redirect('index')
    return render(request, 'pages/registro_proveedor.html')

# Registrar una factura
@login_required
def registro_factura(request):
    facturas = Factura.objects.all()
    return render(request, 'pages/registro_factura.html', {'facturas': facturas})

# Registrar un empleado
@login_required
def registro_empleado(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cargo = request.POST.get('cargo')
        usuario = request.user
        Empleado.objects.create(nombre=nombre, apellido=apellido, cargo=cargo, usuario=usuario)
        return redirect('index')
    return render(request, 'pages/registro_empleado.html')

# Registrar un servicio
@login_required
def registro_servicio(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        Servicio.objects.create(nombre=nombre, descripcion=descripcion, precio=precio)
        return redirect('index')
    return render(request, 'pages/registro_servicio.html')

# Registrar una orden de pedido
@login_required
def registro_orden_pedido(request):
    if request.method == 'POST':
        proveedor_id = request.POST.get('proveedor')
        productos = request.POST.get('productos')
        total = request.POST.get('total')
        proveedor = get_object_or_404(Proveedor, pk=proveedor_id)
        OrdenPedido.objects.create(proveedor=proveedor, productos=productos, total=total)
        return redirect('index')
    proveedores = Proveedor.objects.all()
    return render(request, 'pages/registro_orden_pedido.html', {'proveedores': proveedores})

# Registrar la recepción de productos
@login_required
def registro_recepcion_producto(request):
    if request.method == 'POST':
        orden_pedido_id = request.POST.get('orden_pedido')
        productos_recibidos = request.POST.get('productos_recibidos')
        orden_pedido = get_object_or_404(OrdenPedido, pk=orden_pedido_id)
        RecepcionProducto.objects.create(orden_pedido=orden_pedido, productos_recibidos=productos_recibidos)
        return redirect('index')
    ordenes_pedido = OrdenPedido.objects.all()
    return render(request, 'pages/registro_recepcion_producto.html', {'ordenes_pedido': ordenes_pedido})
def habitaciones_view(request):
    return render(request, 'pages/habitaciones.html')

def restaurante_view(request):
    return render(request, 'pages/restaurante.html')