# Generated by Django 5.0.4 on 2024-04-07 20:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("genre_name", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("genre_name",),
            },
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("material_name", models.CharField(max_length=255)),
            ],
            options={
                "ordering": ("material_name",),
            },
        ),
        migrations.CreateModel(
            name="Painting",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=255, null=True)),
                ("creation_year", models.IntegerField()),
                ("image_url", models.CharField(max_length=255)),
                (
                    "artist",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="artists",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "genre",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="genres",
                        to="gallery.genre",
                    ),
                ),
                (
                    "materials",
                    models.ManyToManyField(
                        related_name="paintings", to="gallery.material"
                    ),
                ),
            ],
            options={
                "ordering": ("title",),
            },
        ),
    ]