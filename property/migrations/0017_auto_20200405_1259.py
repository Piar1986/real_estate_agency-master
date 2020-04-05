# Generated by Django 3.0.4 on 2020-04-05 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0016_auto_20200405_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flat',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='flat_owners', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
