# Generated by Django 2.2.2 on 2019-07-05 04:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_auto_20190702_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 4, 0, 8, 67367, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 5, 4, 0, 8, 67400, tzinfo=utc)),
        ),
    ]
