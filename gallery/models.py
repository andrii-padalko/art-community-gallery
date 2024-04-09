from django.contrib.auth.models import AbstractUser
from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("country_name",)
        verbose_name_plural = "countries"

    def __str__(self):
        return self.country_name


class City(models.Model):
    city_name = models.CharField(max_length=255)
    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        related_name="countries"
    )

    class Meta:
        ordering = ("city_name",)
        verbose_name_plural = "cities"

    def __str__(self):
        return f"{self.city_name}, {self.country}"


class Artist(AbstractUser):
    city = models.ForeignKey(
        City,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="cities"
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Genre(models.Model):
    genre_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("genre_name",)

    def __str__(self):
        return self.genre_name


class Style(models.Model):
    style_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("style_name",)

    def __str__(self):
        return self.style_name


class Material(models.Model):
    material_name = models.CharField(max_length=255)

    class Meta:
        ordering = ("material_name",)

    def __str__(self):
        return self.material_name


class Painting(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.SET_NULL,
        null=True,
        related_name="artists"
    )
    title = models.CharField(max_length=255, blank=True, null=True)
    creation_year = models.IntegerField()
    genre = models.ForeignKey(
        Genre,
        on_delete=models.SET_NULL,
        null=True,
        related_name="genres"
    )
    style = models.ForeignKey(
        Style,
        on_delete=models.SET_NULL,
        null=True,
        related_name="styles"
    )
    materials = models.ManyToManyField(Material, related_name="paintings")
    image_url = models.CharField(max_length=255, null=True, blank=True, )

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title
