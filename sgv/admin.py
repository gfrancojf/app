from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.utils.html import format_html
from . models import Access, Empresa, Cargo, Departaments, Invitado


# Register your models here.
@admin.register(Empresa)
class GestionEmpresa(admin.ModelAdmin):
   list_display = ( 'id','nEmpresa', 'clase_rif', 'rif','naCronimo','logoImg',)
   list_display_links = ('nEmpresa',)


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


class AccesoResource(resources.ModelResource):
    fields= (
        'id',
        'nInvitado',
        'empresa',
        'nOficina',
        'nDepartamentos',
        'fEntrada',
        'equipos',
        'marca',
        'serial',
    )
    class Meta:
        model = Access

@admin.register(Access)
class GestionAcesso(ImportExportModelAdmin):
    resource_classes = [AccesoResource]
    list_display = ('id','nInvitado','empresa','nOficina','nDepartamentos','fEntrada','equipos','marca','serial',)


