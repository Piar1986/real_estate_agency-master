# Generated by Django 3.0.4 on 2020-03-30 07:12

from django.db import migrations
from django.apps import apps

def load_owner_flats(apps, schema_editor):
    Flat = apps.get_model('property','Flat')
    Owner = apps.get_model('property','Owner')
    for flat in Flat.objects.all():
        owner = Owner.objects.get_or_create(name=flat.owner_deprecated, phone_pure=flat.owner_phone_pure)
        owner_flat = owner[0].flat
        owner_flat.set([flat])

def load_flat_owners(apps, schema_editor):
    Flat = apps.get_model('property','Flat')
    Owner = apps.get_model('property','Owner')
    for owner in Owner.objects.all():
        flat = Flat.objects.get_or_create(owner_deprecated=owner.name, owner_phone_pure=owner.phone_pure)
        flat_owner = flat[0].owner
        flat_owner.set([owner])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_flat_owner'),
    ]

    operations = [
        migrations.RunPython(load_owner_flats, load_flat_owners,),
    ]