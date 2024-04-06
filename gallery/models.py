from django.contrib.auth.models import AbstractUser
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

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
        related_name="cities"
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
