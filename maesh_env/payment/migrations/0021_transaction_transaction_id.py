# Generated by Django 2.2.2 on 2019-08-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0020_auto_20190807_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='transaction_id',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
    ]