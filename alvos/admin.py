from django.contrib import admin
from .models import Alvo

@admin.register(Alvo)
class AlvoAdmin(admin.ModelAdmin):
    list_display = ('identificador', 'nome', 'latitude', 'longitude', 'data_expiracao')