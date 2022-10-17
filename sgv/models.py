from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
   # status = models.BooleanField('Estatus', default=True)
    created_at = models.DateField('Fecha de Registro', auto_now = False, auto_now_add = True)
    updated_at = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    deleted_at = models.DateField('Fecha de Eliminacion', auto_now = True, auto_now_add = False)
 
    class Meta:
        abstract = True
class Empresa(BaseModel):
    nEmbresa = models.CharField('Razon Social', max_length=60, unique=True, null=False, blank=False)
    tiporif = [('V', 'Natural de la República Bolivariana de Venezuela'),
               ('J', 'Personal Jurídica'),
               ('G', 'Ente Gubernamental'),
               ('E','Extranjero con residencia en Venezuela'),
               ('P', 'Agente Registrado Con Pasaporte'),                   
               ]
    clase_rif = models.CharField('Estatus del Empleado', max_length=1, choices=tiporif, null=False, default='G')
    rif = models.CharField('RIF', max_length=10, unique=True, null=False, blank=False)
    naCronimo = models.CharField('Acronimo', max_length=60, unique=True, null=True, blank=True)
    logoImg = models.ImageField('LOGOTIPO', null=True, blank=True, upload_to='empresa/logo')
    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
    def __str__(self) -> str:
        return self.nEmbresa 

class Departaments(BaseModel):
    Nempresa = models.ForeignKey(Empresa,verbose_name="Empresa" ,on_delete=models.CASCADE)
    nOficina = models.CharField('Oficina a Visitar', max_length=30, unique=True, null=True, blank=True)
    extTelefono =  PhoneNumberField(blank=True, help_text='Contact phone number')
    class Meta:
        verbose_name = 'Departamento'
        verbose_name_plural = 'Departamentos '

    def __str__(self) -> str:
        return self.nOficina 

class Cargo(BaseModel):
    nDepartamentos = models.ForeignKey(Departaments, on_delete=models.CASCADE)
    nCargo = models.CharField('Cargo', max_length=50)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'
    
    def __str__(self):
        return self.nCargo
    