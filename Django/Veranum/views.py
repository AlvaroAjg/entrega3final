<<<<<<< HEAD
from django.http import HttpResponseForbidden

from django.shortcuts import render, get_object_or_404, redirect


from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Cliente, Proveedor, Producto
from django.views.generic import CreateView
from .models import Cliente
from .models import Empleado
from .models import Factura
from .models import OrdenPedido
from .models import RecepcionProducto
from .models import ReservaHora
from .models import Servicio
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib import messages
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import ListView


=======
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Cliente, ReservaHora, Habitacion, Proveedor, Factura, Empleado, Servicio, OrdenPedido, RecepcionProducto
from .forms import ReservaHoraForm, HabitacionForm
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b

# Página principal
def index(request):
    return render(request, 'pages/index.html')

# Vista para iniciar sesión
def login_view(request):
<<<<<<< HEAD
    return render(request, 'pages/login.html')

def actividades_view(request):
    return render(request, 'pages/actividades.html')

def restaurante_view(request):
    return render(request, 'pages/restaurante.html')

def inicio_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pages/dash')  # Cambia 'dashboard' por la página a la que quieres redirigir
        else:
            messages.error(request, 'Credenciales incorrectas')  # Mensaje para credenciales inválidas
            return render(request, 'pages/inicio.html')  # Muestra el formulario nuevamente

    return render(request, 'pages/inicio.html')

def dash_view(request):
    # Lógica adicional, si es necesario
    return render(request, 'pages/dash.html')




def panel_view(request):
    return render(request, 'pages/panel.html')



class ServiciosView(TemplateView):
    template_name = 'pages/servicios.html'

class CrudView(TemplateView):
    template_name = 'crud.html'    
=======
    return render(request, 'registration/login.html')

# Vista para cerrar sesión
def logout_view(request):
    return redirect('index')

# CRUD para Habitaciones
@login_required
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b

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

<<<<<<< HEAD








class ClienteListView(ListView):
    model = Cliente
    template_name = 'pages/clientes.html'
    context_object_name = 'clientes'

class ClienteCreateView(CreateView):
    model = Cliente
    template_name = 'pages/registro_cliente.html'
    fields = ['usuario', 'direccion']
    success_url = reverse_lazy('cliente-list')

class FacturaCreateView(CreateView):
    model = Factura
    template_name = 'pages/registro_factura.html'
    fields = ['cliente', 'servicios', 'total', 'estado']
    success_url = '/Veranum/facturas/'

class OrdenPedidoCreateView(CreateView):
    model = OrdenPedido
    template_name = 'pages/registro_orden_pedido.html'
    fields = ['proveedor', 'producto', 'estado']
    success_url = '/Veranum/ordenes_pedido/'    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'pages/registro_empleado.html'
    fields = ['usuario', 'cargo']
    success_url = '/Veranum/empleados/'

class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'pages/proveedores.html'
    context_object_name = 'proveedores'

class ReservaHoraCreateView(CreateView):
    model = ReservaHora
    template_name = 'pages/registro_reserva_hora.html'
    fields = ['cliente', 'servicio', 'fecha_hora', 'estado']
    success_url = '/Veranum/reservas/'    

class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'pages/registro_proveedor.html'
    fields = ['nombre', 'contacto', 'rubro']
    success_url = '/Veranum/proveedores/'

class ServicioCreateView(CreateView):
    model = Servicio
    template_name = 'pages/registro_servicio.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = '/Veranum/servicios/'    

class RecepcionProductoCreateView(CreateView):
    model = RecepcionProducto
    template_name = 'pages/registro_recepcion_producto.html'
    fields = ['orden_pedido', 'producto', 'cantidad', 'estado']
    success_url = '/Veranum/recepciones/'        

class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'pages/registro_proveedor.html'
    fields = ['nombre', 'contacto', 'rubro']
    success_url = reverse_lazy('proveedor-list')

class ProductoListView(ListView):
    model = Producto
    template_name = 'pages/productos.html'
    context_object_name = 'productos'

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'pages/registro_producto.html'
    fields = ['nombre', 'descripcion', 'precio']
    success_url = reverse_lazy('producto-list')

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'pages/dash.html'


def inicio_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dash')  # Redirige a otra página
        else:
            return render(request, 'inicio.html', {'error': 'Credenciales incorrectas'})
    return render(request, 'inicio.html')



=======
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
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b
