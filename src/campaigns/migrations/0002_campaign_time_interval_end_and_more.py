# Generated by Django 5.0.6 on 2024-06-26 18:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("campaigns", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaign",
            name="time_interval_end",
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="campaign",
            name="time_interval_start",
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
