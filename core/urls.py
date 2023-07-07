from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', home, name="home"),
    path('login', LoginView.as_view(template_name='core/login.html'), name="login"),
    path('products', products, name="products"),
    path('user', user, name="user"),
    path('seguimiento', seguimiento, name="seguimiento"),
    path('compras', compras, name="compras"),
    path('tierra', tierra, name="tierra"),
    path('flores', flores, name="flores"),
    path('arbustos', arbustos, name="arbustos"),
    path('logout', logout, name="logout"),
    path('registro', registro, name="registro"),
    path('addtocar/<codigo>', addtocar, name="addtocar"),
    path('dropitem/<codigo>', dropitem, name="dropitem"),
    path('carrito', carrito, name="carrito"),
    path('comprar', comprar, name="comprar"),
    path('historial_compra', historial_compra, name="historial_compra"),
    path('detalle/<int:id>', detalle, name="detalle"),
    path('suscribir', suscribir, name="suscribir"),
    path('limpiar', limpiar),
]
