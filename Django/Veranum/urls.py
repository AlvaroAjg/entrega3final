from django.urls import path
from . import views
<<<<<<< HEAD
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
=======

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add/', views.add_reserva, name='add_reserva'),
    path('delete/<int:pk>/', views.delete_reserva, name='delete_reserva'),
    path('update/<int:pk>/', views.update_reserva, name='update_reserva'),
    path('crudhabitacion/', views.crud_habitacion, name='crudhabitacion'),
    path('registro_cliente/', views.registro_cliente, name='registro_cliente'),
    path('registro_reserva_hora/', views.registro_reserva_hora, name='registro_reserva_hora'),
    path('registro_proveedor/', views.registro_proveedor, name='registro_proveedor'),
    path('registro_factura/', views.registro_factura, name='registro_factura'),
    path('registro_empleado/', views.registro_empleado, name='registro_empleado'),
    path('registro_servicio/', views.registro_servicio, name='registro_servicio'),
    path('registro_orden_pedido/', views.registro_orden_pedido, name='registro_orden_pedido'),
    path('habitaciones/', views.habitaciones_view, name='habitaciones'),
    path('restaurante/', views.restaurante_view, name='restaurante'),
    path('registro_recepcion_producto/', views.registro_recepcion_producto, name='registro_recepcion_producto'),
    path('crud/',views.crud, name='crud'),
]
>>>>>>> 1af8711c33b929ad57d7f3c3cfd5889feed10d7b
