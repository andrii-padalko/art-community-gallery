from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from gallery.models import City, Genre, Material, Painting, Artist, Country


@admin.register(Artist)
class ArtistAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("city",)
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info", {"fields": ("city",)}),)
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "city",
                    )
                },
            ),
        )
    )


@admin.register(Painting)
class PaintingAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("artist",)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("city_name",)
    list_filter = ("country",)


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    search_fields = ("material_name",)


@admin.register(Genre)
class CityAdmin(admin.ModelAdmin):
    search_fields = ("genre_name",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    search_fields = ("country_name",)
