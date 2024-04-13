from django.urls import path

from .views import (
    index,
    ArtistListView, ArtistDetailView, ArtistCreateView, ArtistUpdateView, ArtistDeleteView,
    CityListView, CityCreateView, CityUpdateView, CityDeleteView,
    CountryListView,  CountryCreateView, CountryUpdateView, CountryDeleteView,
    PaintingListView, PaintingDetailView, PaintingCreateView, PaintingUpdateView, PaintingDeleteView,
    GenreListView, GenreCreateView, GenreUpdateView, GenreDeleteView,
    StyleListView, StyleCreateView, StyleUpdateView, StyleDeleteView,
    MaterialListView, MaterialCreateView, MaterialUpdateView, MaterialDeleteView,
)

urlpatterns = [
    path("", index, name="index"),

    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("artists/<int:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("artists/create/", ArtistCreateView.as_view(), name="artist-create"),
    path("artists/<int:pk>/update/", ArtistUpdateView.as_view(), name="artist-update"),
    path("artists/<int:pk>/delete/", ArtistDeleteView.as_view(), name="artist-delete"),

    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/create/", CityCreateView.as_view(), name="city-create"),
    path("cities/<int:pk>/update/", CityUpdateView.as_view(), name="city-update"),
    path("cities/<int:pk>/delete/", CityDeleteView.as_view(), name="city-delete"),

    path("countries/", CountryListView.as_view(), name="country-list"),
    path("countries/create/", CountryCreateView.as_view(), name="country-create"),
    path("countries/<int:pk>/update/", CountryUpdateView.as_view(), name="country-update"),
    path("countries/<int:pk>/delete/", CountryDeleteView.as_view(), name="country-delete"),

    path("paintings/", PaintingListView.as_view(), name="painting-list"),
    path("paintings/<int:pk>/", PaintingDetailView.as_view(), name="painting-detail"),
    path("paintings/create/", PaintingCreateView.as_view(), name="painting-create"),
    path("paintings/<int:pk>/update/", PaintingUpdateView.as_view(), name="painting-update"),
    path("paintings/<int:pk>/delete/", PaintingDeleteView.as_view(), name="painting-delete"),

    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genres-delete"),

    path("styles/", StyleListView.as_view(), name="style-list"),
    path("styles/create/", StyleCreateView.as_view(), name="style-create"),
    path("styles/<int:pk>/update/", StyleUpdateView.as_view(), name="style-update"),
    path("styles/<int:pk>/delete/", StyleDeleteView.as_view(), name="style-delete"),

    path("materials/", MaterialListView.as_view(), name="material-list"),
    path("materials/create/", MaterialCreateView.as_view(), name="material-create"),
    path("materials/<int:pk>/update/", MaterialUpdateView.as_view(), name="material-update"),
    path("materials/<int:pk>/delete/", MaterialDeleteView.as_view(), name="material-delete"),
]

app_name = "gallery"
