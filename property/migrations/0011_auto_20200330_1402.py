# Generated by Django 3.0.4 on 2020-03-30 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20200330_1349'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flat',
            old_name='owner',
            new_name='owner_deprecated',
        ),
    ]