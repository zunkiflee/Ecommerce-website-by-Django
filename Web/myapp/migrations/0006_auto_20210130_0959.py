# Generated by Django 3.0 on 2021-01-30 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20210130_0940'),
    ]

    operations = [
        migrations.RenameField(
            model_name='allproduct',
            old_name='photo',
            new_name='image',
        ),
    ]