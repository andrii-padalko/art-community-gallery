from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from gallery.models import Artist, Painting, City, Country, Genre, Style, Material


def index(request):
    """View function for the home page of the site."""

    num_artists = Artist.objects.count()
    num_paintings = Painting.objects.count()
    num_cities = City.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_artists": num_artists,
        "num_paintings": num_paintings,
        "num_cities": num_cities,
        "num_visits": num_visits + 1,
    }

    return render(request, "gallery/index.html", context=context)


class ArtistListView(generic.ListView):
    model = Artist


class ArtistDetailView(generic.DetailView):
    model = Artist
    queryset = get_user_model().objects.all().select_related("city")


class CityListView(generic.ListView):
    model = City


class CountryListView(generic.ListView):
    model = Country


class GenreListView(generic.ListView):
    model = Genre


class StyleListView(generic.ListView):
    model = Style


class MaterialListView(generic.ListView):
    model = Material


class PaintingListView(generic.ListView):
    model = Painting


class PaintingDetailView(generic.DetailView):
    model = Painting
    queryset = Painting.objects.all().prefetch_related("materials")
