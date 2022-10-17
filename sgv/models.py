from django.db import models

# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key = True)
   # status = models.BooleanField('Estatus', default=True)
    created_at = models.DateField('Fecha de Registro', auto_now = False, auto_now_add = True)
    updated_at = models.DateField('Fecha de Modificación', auto_now = True, auto_now_add = False)
    deleted_at = models.DateField('Fecha de Eliminacion', auto_now = True, auto_now_add = False)
 
    class Meta:
        abstract = True