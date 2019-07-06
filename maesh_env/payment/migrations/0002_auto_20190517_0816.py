# Generated by Django 2.1.2 on 2019-05-17 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=500)),
                ('party_id', models.CharField(max_length=10)),
                ('expire_in', models.CharField(max_length=13)),
                ('token_type', models.CharField(max_length=6)),
                ('refresh_token', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]