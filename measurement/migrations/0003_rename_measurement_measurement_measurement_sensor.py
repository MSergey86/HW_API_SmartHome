# Generated by Django 4.1.3 on 2022-11-15 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_created_at_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='measurement',
            new_name='measurement_sensor',
        ),
    ]
