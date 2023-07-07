from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect
import requests

# Create your views here.

def home(request):
    context = {}
    suscrito(request, context)
    return render(request, 'core/index.html', context)

def login(request):
    return render(request, 'core/login.html')

def products(request):
    plantas = Producto.objects.all()
    return render(request, 'core/products.html',{'plantas':plantas, 'carro':request.session.get("carro",[])})

def user(request):
    return render(request, 'core/user.html')

def seguimiento(request):
    return render(request, 'core/tracking.html')

def compras(request):
    return render(request, 'core/purchase-history.html')

def tierra(request):
    tierras = Tierra.objects.all()
    return render(request, 'core/products-tierra.html',{'tierras':tierras, 'carro':request.session.get("carro",[])})

def flores(request):
    flores = Flores.objects.all()
    return render(request, 'core/products-flores.html', {'flores':flores, 'carro':request.session.get("carro",[])})

def arbustos(request):
    arbustos = Arbustos.objects.all()
    return render(request, 'core/products-arbustos.html', {'arbustos':arbustos, 'carro':request.session.get("carro",[])})

def logout(request):
    return logout_then_login(request, login_url="login")

def registro(request):
    if request.method == "POST":
        registro = Registro(request.POST)
        if registro.is_valid():
            registro.save()
            return redirect(to="login")
    else:
        registro = Registro()
    return render(request, 'core/registro.html',{'form':registro})

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[4] += 1
            item[5] = item[3] * item[4]
            break
    else:
        carro.append([codigo, producto.detalle, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="products")

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[4] > 1:
                item[4] -= 1
                item[5] = item[3] * item[4]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="carrito")

def carrito(request):
    context = {}
    carro = request.session.get("carro", [])
    suscrito(request, context)
    context["carro"] = carro
    return render(request, 'core/carrito.html', context)

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to='login')
    carro = request.session.get("carro", [])
    total = 0
    for item in carro:
        total += item[5]
    venta = Venta()
    venta.cliente = request.user
    venta.total = total
    if suscrito:
        total * 0.95
    else:
        total
    venta.save()
    for item in carro:
        detalle = DetalleVenta()
        detalle.producto = Producto.objects.get(codigo = item[0])
        detalle.precio = item[3]
        detalle.cantidad = item[4]
        detalle.venta = venta
        detalle.save()

        producto = Producto.objects.get(codigo = item[0])
        producto.stock -= item[4]
        producto.save()
        request.session["carro"] = []
    return redirect(to=carrito)

def historial_compra(request):
    if request.user.is_authenticated:
        redirect(to="login")
    compras = Venta.objects.filter(cliente=request.user)
    return render(request, 'core/historial_compra.html', {'compras': compras})

def detalle(request, id):
    try:
        venta = Venta.objects.get(id=id)
        detalles = DetalleVenta.objects.filter(venta=venta)
    except Venta.DoesNotExist:
        detalles = None
    return render(request, "core/detalle.html", {"detalles": detalles})

def suscrito(request, context):
    if request.user.is_authenticated:
        email = request.user.email
        resp =requests.get(f"http://127.0.0.1:8000/api/suscrito/{email}")
        context["suscrito"] = resp.json()["suscrito"]

def suscribir(request):
    context = {}
    if request.method == "POST":
        if request.user.is_authenticated:
            resp =requests.get(f"http://127.0.0.1:8000/api/suscribir/{request.user.email}") 
            context["mensaje"] = resp.json()["mensaje"]
            suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)
    else:
        suscrito(request, context)
        return render(request, 'core/suscripcion.html', context)

def limpiar(request):
    request.session.flush()
    return redirect(to="products")
