# Generated by Django 3.1.7 on 2021-03-31 20:17

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0003_auto_20210331_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='picture',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[139, 156], upload_to='staffpics'),
        ),
    ]
