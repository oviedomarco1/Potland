from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Venta(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(default=datetime.now)
    cliente = models.ForeignKey(to=User, on_delete=models.CASCADE)
    estado_envio = models.CharField(max_length=15, default="EN PREPARACION")
    total = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.cliente.username + " " + str(self.fecha)[0:16]

#class Producto == Plantas
class Producto(models.Model):
    codigo = models.CharField(max_length=4,primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.PositiveIntegerField()
    oferta = models.BooleanField()
    porcentaje_oferta = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200)

    def tachado(self):
        if self.oferta:
            return "$" + str(round(self.precio / (1 - (self.porcentaje_oferta / 100))))
        return ""
    
    #Para mostrar en el tag celeste, arriba del producto.
    def descuento(self):
        if self.oferta:
            return str(self.porcentaje_oferta) + "% Dcto."
        return ""

    def __str__(self):
        return self.detalle + " (" + self.codigo + ")"
    

#class Tierra == Tierra
class Tierra(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.PositiveIntegerField()
    oferta = models.BooleanField()
    porcentaje_oferta = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200)

    def tachado(self):
        if self.oferta:
            return "$" + str(round(self.precio / (1 - (self.porcentaje_oferta / 100))))
        return ""
    
    #Para mostrar en el tag celeste, arriba del producto.
    def descuento(self):
        if self.oferta:
            return str(self.porcentaje_oferta) + "% Dcto."
        return ""

    def __str__(self):
        return self.detalle + " (" + self.codigo + ")"


#class Flores == Flores
class Flores(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.PositiveIntegerField()
    oferta = models.BooleanField()
    porcentaje_oferta = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200)

    def tachado(self):
        if self.oferta:
            return "$" + str(round(self.precio / (1 - (self.porcentaje_oferta / 100))))
        return ""
    
    #Para mostrar en el tag celeste, arriba del producto.
    def descuento(self):
        if self.oferta:
            return str(self.porcentaje_oferta) + "% Dcto."
        return ""

    def __str__(self):
        return self.detalle + " (" + self.codigo + ")"
    

#class Arbustos == Arbustos
class Arbustos(models.Model):
    codigo = models.CharField(max_length=4, primary_key=True)
    detalle = models.CharField(max_length=200)
    precio = models.IntegerField()
    stock = models.PositiveIntegerField()
    oferta = models.BooleanField()
    porcentaje_oferta = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200)

    def tachado(self):
        if self.oferta:
            return "$" + str(round(self.precio / (1 - (self.porcentaje_oferta / 100))))
        return ""
    
    #Para mostrar en el tag celeste, arriba del producto.
    def descuento(self):
        if self.oferta:
            return str(self.porcentaje_oferta) + "% Dcto."
        return ""

    def __str__(self):
        return self.detalle + " (" + self.codigo + ")"
    


class DetalleVenta(models.Model):
    id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(to=Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(to=Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio = models.IntegerField()

    def __str__(self):
        return str(self.id) + " " + self.producto.detalle[0:20] + " " + str(self.venta.id)

    