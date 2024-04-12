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
    CityCreateView,
    CountryCreateView,
    GenreCreateView,
    StyleCreateView,
    MaterialCreateView,
    PaintingCreateView,
    ArtistCreateView
)

urlpatterns = [
    path("", index, name="index"),
    path("artists/", ArtistListView.as_view(), name="artist-list"),
    path("artists/<int:pk>/", ArtistDetailView.as_view(), name="artist-detail"),
    path("artists/create", ArtistCreateView.as_view(), name="artist-create"),
    path("cities/", CityListView.as_view(), name="city-list"),
    path("cities/create", CityCreateView.as_view(), name="city-create"),
    path("countries/", CountryListView.as_view(), name="country-list"),
    path("countries/create", CountryCreateView.as_view(), name="country-create"),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/create", GenreCreateView.as_view(), name="genre-create"),
    path("styles/", StyleListView.as_view(), name="style-list"),
    path("genres/create", StyleCreateView.as_view(), name="style-create"),
    path("materials/", MaterialListView.as_view(), name="material-list"),
    path("materials/create", MaterialCreateView.as_view(), name="material-create"),
    path("paintings/", PaintingListView.as_view(), name="painting-list"),
    path("paintings/<int:pk>/", PaintingDetailView.as_view(), name="painting-detail"),
    path("paintings/create", PaintingCreateView.as_view(), name="painting-create"),
]

app_name = "gallery"
