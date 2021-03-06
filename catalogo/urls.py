
from django.conf.urls import url, include
from rest_framework import routers
from .views.categoria_view import CategoriaViewSet
from .views.producto_view import ProductoViewSet
from .views.menu_view import MenuViewSet
from .views.pedido_view import PedidoViewSet
from .views.cliente_view import ClienteViewSet
from .views.reserva_view import ReservaViewSet
from .views.mesa_view import MesaViewSet
from .views.venta_view import VentaViewSet
from .views.detalleVenta_view import DetalleVentaViewSet


router = routers.DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'menus', MenuViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'mesas', MesaViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detalleVentas', DetalleVentaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
