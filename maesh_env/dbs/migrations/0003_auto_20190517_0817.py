# Generated by Django 2.1.2 on 2019-05-17 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbs', '0002_auto_20190517_0816'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Credentials',
            new_name='Credential',
        ),
    ]
