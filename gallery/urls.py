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
    path("artists/update/<int:pk>/", ArtistUpdateView.as_view(), name="artist-update"),
    path("artists/delete/<int:pk>/", ArtistDeleteView.as_view(), name="artist-delete"),

    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/create/", CityCreateView.as_view(), name="city-create"),
    path("cities/update/<int:pk>/", CityUpdateView.as_view(), name="city-update"),
    path("cities/delete/<int:pk>/", CityDeleteView.as_view(), name="city-delete"),

    path("countries/", CountryListView.as_view(), name="country-list"),
    path("countries/create/", CountryCreateView.as_view(), name="country-create"),
    path("countries/update/<int:pk>/", CountryUpdateView.as_view(), name="country-update"),
    path("countries/delete/<int:pk>/", CountryDeleteView.as_view(), name="country-delete"),

    path("paintings/", PaintingListView.as_view(), name="painting-list"),
    path("paintings/<int:pk>/", PaintingDetailView.as_view(), name="painting-detail"),
    path("paintings/create/", PaintingCreateView.as_view(), name="painting-create"),
    path("paintings/update/<int:pk>/", PaintingUpdateView.as_view(), name="painting-update"),
    path("paintings/delete/<int:pk>/", PaintingDeleteView.as_view(), name="painting-delete"),

    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genres/update/<int:pk>/", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/delete/<int:pk>/", GenreDeleteView.as_view(), name="genres-delete"),

    path("styles/", StyleListView.as_view(), name="style-list"),
    path("styles/create/", StyleCreateView.as_view(), name="style-create"),
    path("styles/update/<int:pk>/", StyleUpdateView.as_view(), name="style-update"),
    path("styles/delete/<int:pk>/", StyleDeleteView.as_view(), name="style-delete"),

    path("materials/", MaterialListView.as_view(), name="material-list"),
    path("materials/create/", MaterialCreateView.as_view(), name="material-create"),
    path("materials/update/<int:pk>/", MaterialUpdateView.as_view(), name="material-update"),
    path("materials/delete/<int:pk>/", MaterialDeleteView.as_view(), name="material-delete"),
]

app_name = "gallery"
