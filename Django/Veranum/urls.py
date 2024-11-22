from django.urls import path
from . import views

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
