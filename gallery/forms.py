from django import forms
from django.contrib.auth.forms import UserCreationForm

from gallery.models import Painting, Material, Artist


class PaintingForm(forms.ModelForm):
    materials = forms.ModelMultipleChoiceField(
        queryset=Material.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Painting
        fields = "__all__"


class ArtistCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Artist
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "city",
        )


class ArtistSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by last name"
            }
        )
    )


class CitySearchForm(forms.Form):
    city_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by city"
            }
        )
    )


class CountrySearchForm(forms.Form):
    country_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by country"
            }
        )
    )


class PaintingSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by title"
            }
        )
    )


class GenreSearchForm(forms.Form):
    genre_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by genre"
            }
        )
    )


class StyleSearchForm(forms.Form):
    style_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by style"
            }
        )
    )


class MaterialSearchForm(forms.Form):
    material_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "search by material"
            }
        )
    )