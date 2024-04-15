from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Artist, Painting, City, Country, Genre, Style, Material
from .forms import (
    PaintingForm,
    ArtistCreationForm,
    ArtistSearchForm,
    CitySearchForm,
    CountrySearchForm,
    PaintingSearchForm,
    GenreSearchForm,
    StyleSearchForm,
    MaterialSearchForm
)


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
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArtistListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["search_form"] = ArtistSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = Artist.objects.all()
        form = ArtistSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(
                last_name__icontains=form.cleaned_data["last_name"]
            )
        return queryset


class ArtistDetailView(LoginRequiredMixin, generic.DetailView):
    model = Artist
    queryset = get_user_model().objects.all().select_related("city")


class ArtistCreateView(LoginRequiredMixin, generic.CreateView):
    model = Artist
    form_class = ArtistCreationForm
    success_url = reverse_lazy("gallery:artist-list")


class ArtistUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Artist
    fields = ["first_name", "last_name", "city"]
    success_url = reverse_lazy("gallery:artist-list")


class ArtistDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Artist
    success_url = reverse_lazy("gallery:artist-list")


class CityListView(LoginRequiredMixin, generic.ListView):
    model = City
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CityListView, self).get_context_data(**kwargs)
        city_name = self.request.GET.get("city_name", "")
        context["search_form"] = CitySearchForm(
            initial={"city_name": city_name}
        )
        return context

    def get_queryset(self):
        queryset = City.objects.all().select_related("country")
        form = CitySearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(city_name__icontains=form.cleaned_data["city_name"])
        return queryset


class CityCreateView(LoginRequiredMixin, generic.CreateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("gallery:city-list")


class CityDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = City
    success_url = reverse_lazy("gallery:city-list")


class CityUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = City
    fields = "__all__"
    success_url = reverse_lazy("gallery:city-list")


class CountryListView(LoginRequiredMixin, generic.ListView):
    model = Country
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CountryListView, self).get_context_data(**kwargs)
        country_name = self.request.GET.get("country_name", "")
        context["search_form"] = CountrySearchForm(
            initial={"country_name": country_name}
        )
        return context

    def get_queryset(self):
        queryset = Country.objects.all()
        form = CountrySearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(country_name__icontains=form.cleaned_data["country_name"])
        return queryset


class CountryCreateView(LoginRequiredMixin, generic.CreateView):
    model = Country
    fields = "__all__"
    success_url = reverse_lazy("gallery:country-list")


class CountryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Country
    fields = "__all__"
    success_url = reverse_lazy("gallery:country-list")


class CountryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Country
    success_url = reverse_lazy("gallery:country-list")


class GenreListView(LoginRequiredMixin, generic.ListView):
    model = Genre
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        genre_name = self.request.GET.get("genre_name", "")
        context["search_form"] = GenreSearchForm(
            initial={"genre_name": genre_name}
        )
        return context

    def get_queryset(self):
        queryset = Genre.objects.all()
        form = GenreSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(genre_name__icontains=form.cleaned_data["genre_name"])
        return queryset


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("gallery:genre-list")


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    fields = "__all__"
    success_url = reverse_lazy("gallery:genre-list")


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("gallery:genre-list")


class StyleListView(LoginRequiredMixin, generic.ListView):
    model = Style
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(StyleListView, self).get_context_data(**kwargs)
        style_name = self.request.GET.get("style_name", "")
        context["search_form"] = StyleSearchForm(
            initial={"style_name": style_name}
        )
        return context

    def get_queryset(self):
        queryset = Style.objects.all()
        form = StyleSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(style_name__icontains=form.cleaned_data["style_name"])
        return queryset


class StyleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Style
    fields = "__all__"
    success_url = reverse_lazy("gallery:style-list")


class StyleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Style
    fields = "__all__"
    success_url = reverse_lazy("gallery:style-list")


class StyleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Style
    success_url = reverse_lazy("gallery:style-list")


class MaterialListView(LoginRequiredMixin, generic.ListView):
    model = Material
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MaterialListView, self).get_context_data(**kwargs)
        material_name = self.request.GET.get("material_name", "")
        context["search_form"] = MaterialSearchForm(
            initial={"material_name": material_name}
        )
        return context

    def get_queryset(self):
        queryset = Material.objects.all()
        form = MaterialSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(material_name__icontains=form.cleaned_data["material_name"])
        return queryset


class MaterialCreateView(LoginRequiredMixin, generic.CreateView):
    model = Material
    fields = "__all__"
    success_url = reverse_lazy("gallery:material-list")


class MaterialUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Material
    fields = "__all__"
    success_url = reverse_lazy("gallery:material-list")


class MaterialDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Material
    success_url = reverse_lazy("gallery:material-list")


class PaintingListView(LoginRequiredMixin, generic.ListView):
    model = Painting
    paginate_by = 5

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PaintingListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = PaintingSearchForm(
            initial={"title": title}
        )
        return context

    def get_queryset(self):
        queryset = Painting.objects.all()
        form = PaintingSearchForm(self.request.GET)
        if form.is_valid():
            return queryset.filter(title__icontains=form.cleaned_data["title"])
        return queryset


class PaintingDetailView(LoginRequiredMixin, generic.DetailView):
    model = Painting
    queryset = Painting.objects.all().prefetch_related("materials")


class PaintingCreateView(LoginRequiredMixin, generic.CreateView):
    model = Painting
    form_class = PaintingForm
    success_url = reverse_lazy("gallery:painting-list")


class PaintingUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Painting
    form_class = PaintingForm
    success_url = reverse_lazy("gallery:painting-list")


class PaintingDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Painting
    success_url = reverse_lazy("gallery:painting-list")
