from django.contrib.auth import get_user_model
from django.test import TestCase

from gallery.models import City, Painting, Genre, Style, Material, Country, AbstractUser


class ModelsTests(TestCase):

    def test_country_str(self):
        country = Country.objects.create(country_name="Test Country")
        self.assertEqual(
            str(country),
            country.country_name
        )

    def test_city_str(self):
        country = Country.objects.create(country_name="Test Country")
        city = City.objects.create(city_name="Test City", country=country)
        self.assertEqual(
            str(city),
            f"{city.city_name}, {city.country}"
        )

    def test_genre_str(self):
        genre = Genre.objects.create(genre_name="Test genre")
        self.assertEqual(
            str(genre),
            genre.genre_name
        )

    def test_style_str(self):
        style = Style.objects.create(style_name="Test style")
        self.assertEqual(
            str(style),
            style.style_name
        )

    def test_material_str(self):
        material = Material.objects.create(material_name="Test material")
        self.assertEqual(
            str(material),
            material.material_name
        )

    def test_painting_str(self):
        painting = Painting.objects.create(
            title="Test title",
            creation_year=2024,
        )
        self.assertEqual(
            str(painting),
            painting.title
        )

    def test_artist_str(self):
        country = Country.objects.create(country_name="Test Country")
        city = City.objects.create(city_name="Test City", country=country)
        artist = get_user_model().objects.create(
            username="test_user",
            password="test1234",
            first_name="test_first",
            last_name="test_last",
            city=city
        )
        self.assertEqual(
            str(artist),
            f"{artist.first_name} {artist.last_name} ({artist.username})"
        )

    def test_artist_with_city(self):
        country = Country.objects.create(country_name="Test Country")
        city = City.objects.create(city_name="Test City", country=country)
        username = "test_username"
        password = "test1234"
        artist = get_user_model().objects.create_user(
            username=username,
            password=password,
            city=city
        )
        self.assertEqual(artist.username, username)
        self.assertEqual(artist.city, city)
        self.assertTrue(artist.check_password(password))
