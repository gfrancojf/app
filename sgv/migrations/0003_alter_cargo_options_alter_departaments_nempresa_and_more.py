# Generated by Django 4.1.2 on 2022-10-17 18:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sgv', '0002_empresa_nacronimo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cargo',
            options={'verbose_name': 'Cargo', 'verbose_name_plural': 'Cargos'},
        ),
        migrations.AlterField(
            model_name='departaments',
            name='Nempresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sgv.empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='empresa',
            name='clase_rif',
            field=models.CharField(choices=[('V', 'Natural de la República Bolivariana de Venezuela'), ('J', 'Personal Jurídica'), ('G', 'Ente Gubernamental'), ('E', 'Extranjero con residencia en Venezuela'), ('P', 'Agente Registrado Con Pasaporte')], default='G', max_length=1, verbose_name='Estatus del Empleado'),
        ),
    ]