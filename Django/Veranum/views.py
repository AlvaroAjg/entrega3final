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



# Create your views here.

def index(request):
    context={
        "usuario":"nico"
    }
    return render(request, 'pages/index.html', context)

def login_view(request):
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



