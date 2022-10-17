from django.contrib import admin
from django.utils.html import format_html
from . models import Empresa, Cargo, Departaments


# Register your models here.
@admin.register(Empresa)
class GestionEmpresa(admin.ModelAdmin):
   list_display = ( 'id','nEmbresa', 'clase_rif', 'rif','naCronimo','logoImg',)
   list_display_links = ('nEmbresa',)


@admin.register(Departaments)
class GestionDepartaments(admin.ModelAdmin):
   list_display = ( 'id','Nempresa','nOficina','extTelefono',)
   list_display_links = ('nOficina',)


@admin.register(Cargo)
class GestionCargo(admin.ModelAdmin):
    list_display = ('id',)