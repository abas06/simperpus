# Generated by Django 5.0.7 on 2024-08-02 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpus_app', '0002_authgroup_authgrouppermissions_authpermission_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PerpusAppMasterbuku',
        ),
        migrations.AlterModelOptions(
            name='masterbuku',
            options={'managed': True},
        ),
        migrations.AlterModelOptions(
            name='mastersumberbuku',
            options={'managed': True},
        ),
    ]
