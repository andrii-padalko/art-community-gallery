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
