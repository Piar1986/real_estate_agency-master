# Generated by Django 3.0.4 on 2020-03-30 06:13

from django.conf import settings
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0006_auto_20200330_1258'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Complaints',
            new_name='Complaint',
        ),
        migrations.AddField(
            model_name='flat',
            name='owner_phone_pure',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
