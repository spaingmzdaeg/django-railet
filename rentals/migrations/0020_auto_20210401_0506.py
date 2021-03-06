# Generated by Django 3.1.7 on 2021-04-01 05:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0019_auto_20210401_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='manager_staff',
            field=models.OneToOneField(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='store_managed_by_me', to='rentals.staff'),
            preserve_default=False,
        ),
    ]
