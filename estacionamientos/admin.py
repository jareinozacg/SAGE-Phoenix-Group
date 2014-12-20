from django.contrib import admin

# Register your models here.
from estacionamientos.models import Estacionamiento, Reserva, Pago

admin.site.register(Estacionamiento)
admin.site.register(Reserva)
admin.site.register(Pago)