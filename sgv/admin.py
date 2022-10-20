from django.contrib import admin
from django.utils.html import format_html
from . models import Access, Empresa, Cargo, Departaments, Herramientas, Invitado


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
    list_display = ('id','nDepartamentos','nCargo','nGerente',)

@admin.register(Invitado)
class GestionInvitado(admin.ModelAdmin):
    list_display = ('id', 'cedula','nombre',)
    list_display_links = ('cedula',)


@admin.register(Herramientas)
class GestionHerramientas(admin.ModelAdmin):
    list_display = ('serial','marca','equipos')
    list_display_links = ('marca',)


@admin.register(Access)
class GestionAcesso(admin.ModelAdmin):
    list_display = ('id','cedula','nDepartamento','nCargo','fEntrada','FSalida',)
    list_display_links = ('cedula',)