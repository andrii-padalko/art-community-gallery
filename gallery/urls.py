from django.urls import path

from .views import (
    index,
    ArtistListView,
    ArtistDetailView,
    CityListView,
    CountryListView,
    GenreListView,
    StyleListView,
    MaterialListView,
    PaintingListView,
    PaintingDetailView,


)

urlpatterns = [
    path("", index, name="index"),
    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("artists/<int:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("countries/", CountryListView.as_view(), name="country-list"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("styles/", StyleListView.as_view(), name="style-list"),
    path("materials/", MaterialListView.as_view(), name="material-list"),
    path("paintings/", PaintingListView.as_view(), name="painting-list"),
    path("paintings/<int:pk>/", PaintingDetailView.as_view(), name="painting-detail"),
]

app_name = "gallery"
