from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path
from .views import ClienteListView, ClienteCreateView, ProveedorListView, ProveedorCreateView, ProductoListView, ProductoCreateView
from .views import EmpleadoCreateView
from .views import FacturaCreateView
from .views import OrdenPedidoCreateView
from .views import ProveedorCreateView
from .views import RecepcionProductoCreateView
from .views import ReservaHoraCreateView
from .views import ServicioCreateView
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import DashboardView
from .views import inicio_view
from . import views
from .views import ServiciosView

urlpatterns = [path('', views.index,name='index'),
    path('inicio/', views.login_view, name='inicio'), 
    path('actividades', views.actividades_view, name= 'actividades'),
    path('restaurante', views.restaurante_view, name= 'restaurante'),
    path('servicios/', ServiciosView.as_view(), name='servicios'),
    path('panel', views.panel_view, name= 'panel'),
    path('crud/', views.CrudView.as_view(), name='crud'),
  
    path('dash/', views.dash_view, name='dash'),
    


    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/nuevo/', ClienteCreateView.as_view(), name='cliente-create'),
    path('registro_cliente/', ClienteCreateView.as_view(), name='registro-cliente'),
    path('registro_factura/', FacturaCreateView.as_view(), name='registro-factura'),
    path('registro_empleado/', EmpleadoCreateView.as_view(), name='registro-empleado'),
    path('registro_orden_pedido/', OrdenPedidoCreateView.as_view(), name='registro-orden-pedido'),
    path('registro_proveedor/', ProveedorCreateView.as_view(), name='registro-proveedor'),
    path('registro_recepcion_producto/', RecepcionProductoCreateView.as_view(), name='registro-recepcion-producto'),
    path('proveedores/', ProveedorListView.as_view(), name='proveedor-list'),
    path('registro_reserva_hora/', ReservaHoraCreateView.as_view(), name='registro-reserva-hora'),
    path('registro_servicio/', ServicioCreateView.as_view(), name='registro-servicio'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedor-create'),
    path('productos/', ProductoListView.as_view(), name='producto-list'),
    path('productos/nuevo/', ProductoCreateView.as_view(), name='producto-create'),
    path('inicio/', inicio_view, name='inicio'),
    

   


    







    ]