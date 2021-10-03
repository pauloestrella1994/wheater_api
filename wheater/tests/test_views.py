import pytest
from _pytest.python import pytest_generate_tests
from django.http import response
from django.test import RequestFactory, TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from wheater.models import Wheater
from wheater.tests.conftest import wheater_one
from wheater.views import WheatersView, WheaterView


class TestWheatersView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_wheater_view(self):
        path = reverse('wheater')
        mixer.blend(
            Wheater,
            date="2019-06-11",
            lat=41.8818,
            lon=-87.6231,
            city="Chicago",
            state="Illinois",
            temperatures=[24.0, 21.5, 24.0, 19.5, 25.5]
        )
        response = self.client.get(path)
        response_data = {
            "id": 1,
            "date": "2019-06-11",
            "lat": 41.8818,
            "lon": -87.6231,
            "city": "Chicago",
            "state": "Illinois",
            "temperatures": [24.0, 21.5, 24.0, 19.5, 25.5]
        }
        assert response.status_code == 200
        assert response.json()[0] == response_data





@pytest.mark.django_db
class TestWheaterView:
    def test_wheaterbyid_view(self):
        pass
