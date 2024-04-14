from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from gallery.models import City, Country


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            username="admin",
            password="test1234"
        )
        self.client.force_login(self.admin_user)
        country = Country.objects.create(country_name="Test Country")
        city = City.objects.create(city_name="Test City", country=country)
        self.artist = get_user_model().objects.create_user(
            username="artist",
            password="test1234",
            city=city
        )

    def test_city_name_listed(self):
        url = reverse("admin:gallery_artist_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.artist.city)

    def test_artist_detail_city_name_listed(self):
        url = reverse("admin:gallery_artist_change", args=[self.artist.id])
        res = self.client.get(url)
        self.assertContains(res, self.artist.city)
