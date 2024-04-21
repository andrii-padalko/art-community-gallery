from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from gallery.models import Artist, Country, City, Painting, Genre, Style, Material

COUNTRY_LIST_URL = reverse("gallery:country-list")
CITY_LIST_URL = reverse("gallery:city-list")
PAINTING_LIST_URL = reverse("gallery:painting-list")
GENRE_LIST_URL = reverse("gallery:genre-list")
STYLE_LIST_URL = reverse("gallery:style-list")
MATERIAL_LIST_URL = reverse("gallery:material-list")
ARTIST_LIST_URL = reverse("gallery:artist-list")
ARTIST_CREATE_URL = reverse("gallery:artist-create")


class PublicCityTests(TestCase):
    def test_login_required(self):
        response = self.client.get(CITY_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCityTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        City.objects.create(city_name="Test City 01")
        City.objects.create(city_name="Test City 02")
        City.objects.create(city_name="Another City")

    def test_retrieve_city(self):
        response = self.client.get(CITY_LIST_URL)
        self.assertEqual(response.status_code, 200)
        cities = City.objects.all()
        self.assertEqual(
            list(response.context["city_list"]),
            list(cities)
        )

    def test_searching_city_find_existing_and_relevant(self):
        response = self.client.get(CITY_LIST_URL, {"city_name": "Test"})
        self.assertContains(response, "Test City 01")
        self.assertContains(response, "Test City 02")
        self.assertNotContains(response, "Another City")

    def test_searching_city_doesnt_find_not_existing(self):
        response = self.client.get(CITY_LIST_URL, {"city_name": "noname"})
        self.assertNotContains(response, "Test City 01")
        self.assertNotContains(response, "Test City 02")
        self.assertNotContains(response, "Another City")

    def test_searching_city_find_all_if_name_empty(self):
        response = self.client.get(CITY_LIST_URL, {"city_name": ""})
        self.assertContains(response, "Test City 01")
        self.assertContains(response, "Test City 02")
        self.assertContains(response, "Another City")


class PublicCountryTests(TestCase):
    def test_login_required(self):
        response = self.client.get(COUNTRY_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateCountryTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        Country.objects.create(country_name="Test Country 01")
        Country.objects.create(country_name="Test Country 02")
        Country.objects.create(country_name="Another Country")

    def test_retrieve_country(self):
        response = self.client.get(COUNTRY_LIST_URL)
        self.assertEqual(response.status_code, 200)
        countries = Country.objects.all()
        self.assertEqual(
            list(response.context["country_list"]),
            list(countries)
        )

    def test_searching_country_find_existing_and_relevant(self):
        response = self.client.get(COUNTRY_LIST_URL, {"country_name": "Test"})
        self.assertContains(response, "Test Country 01")
        self.assertContains(response, "Test Country 02")
        self.assertNotContains(response, "Another Country")

    def test_searching_country_doesnt_find_not_existing(self):
        response = self.client.get(COUNTRY_LIST_URL, {"country_name": "noname"})
        self.assertNotContains(response, "Test Country 01")
        self.assertNotContains(response, "Test Country 02")
        self.assertNotContains(response, "Another Country")

    def test_searching_country_find_all_if_name_empty(self):
        response = self.client.get(COUNTRY_LIST_URL, {"country_name": ""})
        self.assertContains(response, "Test Country 01")
        self.assertContains(response, "Test Country 02")
        self.assertContains(response, "Another Country")


class PublicPaintingTests(TestCase):
    def test_login_required(self):
        response = self.client.get(PAINTING_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivatePaintingTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        Painting.objects.create(title="Test Painting 01", creation_year=1931)
        Painting.objects.create(title="Test Painting 02", creation_year=1845)
        Painting.objects.create(title="Another Painting", creation_year=2024)

    def test_retrieve_painting(self):
        response = self.client.get(PAINTING_LIST_URL)
        self.assertEqual(response.status_code, 200)
        paintings = Painting.objects.all()
        self.assertEqual(
            list(response.context["painting_list"]),
            list(paintings)
        )

    def test_searching_painting_find_existing_and_relevant(self):
        response = self.client.get(PAINTING_LIST_URL, {"title": "Test"})
        self.assertContains(response, "Test Painting 01")
        self.assertContains(response, "Test Painting 02")
        self.assertNotContains(response, "Another Painting")

    def test_searching_painting_doesnt_find_not_existing(self):
        response = self.client.get(PAINTING_LIST_URL, {"title": "noname"})
        self.assertNotContains(response, "Test Painting 01")
        self.assertNotContains(response, "Test Painting 02")
        self.assertNotContains(response, "Another Painting")

    def test_searching_painting_find_all_if_title_empty(self):
        response = self.client.get(PAINTING_LIST_URL, {"title": ""})
        self.assertContains(response, "Test Painting 01")
        self.assertContains(response, "Test Painting 02")
        self.assertContains(response, "Another Painting")


class PublicMaterialTests(TestCase):
    def test_login_required(self):
        response = self.client.get(MATERIAL_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateMaterialTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        Material.objects.create(material_name="Test Material 01")
        Material.objects.create(material_name="Test Material 02")
        Material.objects.create(material_name="Another Material")

    def test_retrieve_material(self):
        response = self.client.get(MATERIAL_LIST_URL)
        self.assertEqual(response.status_code, 200)
        materials = Material.objects.all()
        self.assertEqual(
            list(response.context["material_list"]),
            list(materials)
        )

    def test_searching_material_find_existing_and_relevant(self):
        response = self.client.get(MATERIAL_LIST_URL, {"material_name": "Test"})
        self.assertContains(response, "Test Material 01")
        self.assertContains(response, "Test Material 02")
        self.assertNotContains(response, "Another Material")

    def test_searching_material_doesnt_find_not_existing(self):
        response = self.client.get(MATERIAL_LIST_URL, {"material_name": "noname"})
        self.assertNotContains(response, "Test Material 01")
        self.assertNotContains(response, "Test Material 02")
        self.assertNotContains(response, "Another Material")

    def test_searching_material_find_all_if_name_empty(self):
        response = self.client.get(MATERIAL_LIST_URL, {"material_name": ""})
        self.assertContains(response, "Test Material 01")
        self.assertContains(response, "Test Material 02")
        self.assertContains(response, "Another Material")


class PublicStyleTests(TestCase):
    def test_login_required(self):
        response = self.client.get(STYLE_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateStyleTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        Style.objects.create(style_name="Test Style 01")
        Style.objects.create(style_name="Test Style 02")
        Style.objects.create(style_name="Another Style")

    def test_retrieve_style(self):
        response = self.client.get(STYLE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        styles = Style.objects.all()
        self.assertEqual(
            list(response.context["style_list"]),
            list(styles)
        )

    def test_searching_style_find_existing_and_relevant(self):
        response = self.client.get(STYLE_LIST_URL, {"style_name": "Test"})
        self.assertContains(response, "Test Style 01")
        self.assertContains(response, "Test Style 02")
        self.assertNotContains(response, "Another Style")

    def test_searching_style_doesnt_find_not_existing(self):
        response = self.client.get(STYLE_LIST_URL, {"style_name": "noname"})
        self.assertNotContains(response, "Test Style 01")
        self.assertNotContains(response, "Test Style 02")
        self.assertNotContains(response, "Another Style")

    def test_searching_style_find_all_if_name_empty(self):
        response = self.client.get(STYLE_LIST_URL, {"style_name": ""})
        self.assertContains(response, "Test Style 01")
        self.assertContains(response, "Test Style 02")
        self.assertContains(response, "Another Style")


class PublicGenreTests(TestCase):
    def test_login_required(self):
        response = self.client.get(GENRE_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateGenreTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        Genre.objects.create(genre_name="Test Genre 01")
        Genre.objects.create(genre_name="Test Genre 02")
        Genre.objects.create(genre_name="Another Genre")

    def test_retrieve_genre(self):
        response = self.client.get(GENRE_LIST_URL)
        self.assertEqual(response.status_code, 200)
        genres = Genre.objects.all()
        self.assertEqual(
            list(response.context["genre_list"]),
            list(genres)
        )

    def test_searching_genre_find_existing_and_relevant(self):
        response = self.client.get(GENRE_LIST_URL, {"genre_name": "Test"})
        self.assertContains(response, "Test Genre 01")
        self.assertContains(response, "Test Genre 02")
        self.assertNotContains(response, "Another Genre")

    def test_searching_genre_doesnt_find_not_existing(self):
        response = self.client.get(GENRE_LIST_URL, {"genre_name": "noname"})
        self.assertNotContains(response, "Test Genre 01")
        self.assertNotContains(response, "Test Genre 02")
        self.assertNotContains(response, "Another Genre")

    def test_searching_genre_find_all_if_name_empty(self):
        response = self.client.get(GENRE_LIST_URL, {"genre_name": ""})
        self.assertContains(response, "Test Genre 01")
        self.assertContains(response, "Test Genre 02")
        self.assertContains(response, "Another Genre")


class PublicArtistTests(TestCase):
    def test_login_required(self):
        response = self.client.get(ARTIST_LIST_URL)
        self.assertNotEqual(response.status_code, 200)


class PrivateArtistTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="test_user",
            password="test1234"
        )
        self.client.force_login(self.user)
        get_user_model().objects.create_user(
            username="somebody_01",
            password="test123",
            first_name="Test_01",
            last_name="Test Artist 01"
        )
        get_user_model().objects.create_user(
            username="somebody_02",
            password="test123",
            first_name="Test_02",
            last_name="Test Artist 02"
        )
        get_user_model().objects.create_user(
            username="somebody_03",
            password="test123",
            first_name="Another",
            last_name="Another Artist"
        )

    def test_retrieve_style(self):
        response = self.client.get(ARTIST_LIST_URL)
        self.assertEqual(response.status_code, 200)
        styles = Artist.objects.all()
        self.assertEqual(
            list(response.context["artist_list"]),
            list(styles)
        )

    def test_create_artist(self):
        country = Country.objects.create(country_name="Test Country")
        city = City.objects.create(city_name="Test City", country=country)
        form_data = {
            "username": "new_user",
            "password1": "user1234test",
            "password2": "user1234test",
            "first_name": "Test first",
            "last_name": "Test last",
            "city": city.id,
        }
        self.client.post(ARTIST_CREATE_URL, data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])
        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(new_user.city.id, form_data["city"])

    def test_searching_artist_find_existing_and_relevant(self):
        response = self.client.get(ARTIST_LIST_URL, {"last_name": "Test"})
        self.assertContains(response, "Test Artist 01")
        self.assertContains(response, "Test Artist 02")
        self.assertNotContains(response, "Another Artist")

    def test_searching_artist_doesnt_find_not_existing(self):
        response = self.client.get(ARTIST_LIST_URL, {"last_name": "noname"})
        self.assertNotContains(response, "Test Artist 01")
        self.assertNotContains(response, "Test Artist 02")
        self.assertNotContains(response, "Another Artist")

    def test_searching_artist_find_all_if_last_name_empty(self):
        response = self.client.get(ARTIST_LIST_URL, {"last_name": ""})
        self.assertContains(response, "Test Artist 01")
        self.assertContains(response, "Test Artist 02")
        self.assertContains(response, "Another Artist")
