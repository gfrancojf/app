# Generated by Django 4.1.2 on 2022-10-17 19:04

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('sgv', '0003_alter_cargo_options_alter_departaments_nempresa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departaments',
            name='extTelefono',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, help_text='Contact phone number', max_length=128, region=None),
        ),
    ]
