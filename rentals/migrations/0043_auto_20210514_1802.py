# Generated by Django 3.1.7 on 2021-05-14 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0042_auto_20210514_0250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='password',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='username',
        ),
    ]