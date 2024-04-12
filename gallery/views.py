from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Artist, Painting, City, Country, Genre, Style, Material
from .forms import PaintingForm, ArtistCreationForm


@login_required
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


class ArtistListView(LoginRequiredMixin, generic.ListView):
    model = Artist
    paginate_by = 4


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = Artist
    queryset = get_user_model().objects.all().select_related("city")


class ArtistCreateView(LoginRequiredMixin, generic.CreateView):
    model = Artist
    form_class = ArtistCreationForm


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City


class CityCreateView(LoginRequiredMixin, generic.CreateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("gallery:city-list")


class CountryListView(LoginRequiredMixin, generic.ListView):
    model = Country


class CountryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Country
    fields = "__all__"
    success_url = reverse_lazy("gallery:country-list")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("gallery:genre-list")


class StyleListView(LoginRequiredMixin, generic.ListView):
    model = Style


class StyleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Style
    fields = "__all__"
    success_url = reverse_lazy("gallery:style-list")


class MaterialListView(LoginRequiredMixin, generic.ListView):
    model = Material


class MaterialCreateView(LoginRequiredMixin, generic.CreateView):
    model = Material
    fields = "__all__"
    success_url = reverse_lazy("gallery:material-list")


class PaintingListView(LoginRequiredMixin, generic.ListView):
    model = Painting
    paginate_by = 4


class PaintingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Painting
    queryset = Painting.objects.all().prefetch_related("materials")


class PaintingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Painting
    form_class = PaintingForm
    success_url = reverse_lazy("gallery:painting-list")
