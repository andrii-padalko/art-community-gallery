# Generated by Django 5.0.4 on 2024-04-08 17:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0003_country_alter_city_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artist",
            name="city",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="cities",
                to="gallery.city",
            ),
        ),
    ]