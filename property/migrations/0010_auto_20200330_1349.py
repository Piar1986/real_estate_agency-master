# Generated by Django 3.0.4 on 2020-03-30 06:49

from django.db import migrations
from django.apps import apps
from property.models import Flat
from property.models import Owner

def load_owners(apps, schema_editor):
    Owner = apps.get_model('property','Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(phone_pure=flat.owner_phone_pure, defaults={
            'name': flat.owner,
            'phonenumber': flat.owners_phonenumber,
        })

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_owner'),
    ]

    operations = [
        migrations.RunPython(load_owners,),
    ]