# Generated by Django 2.1.2 on 2019-05-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20190521_0706'),
    ]

    operations = [
        migrations.AddField(
            model_name='credential',
            name='cin_party_id',
            field=models.CharField(default='Q0lOMDAwMDAx', max_length=13),
            preserve_default=False,
        ),
    ]