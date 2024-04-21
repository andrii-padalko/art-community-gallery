from django.test import TestCase

from gallery.forms import ArtistCreationForm
from gallery.models import Country, City


class FormsTests(TestCase):
    def test_artist_creation_form_with_is_valid(self):
        country = Country.objects.create(country_name="Test Country")
        city = City.objects.create(city_name="Test City", country=country)
        form_data = {
            "username": "new_user",
            "password1": "user1234test",
            "password2": "user1234test",
            "first_name": "Test first",
            "last_name": "Test last",
            "city": city
        }
        form = ArtistCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)
