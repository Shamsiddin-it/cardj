# Generated by Django 5.0 on 2024-10-29 10:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=None),
            preserve_default=False,
        ),
    ]