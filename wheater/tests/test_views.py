import pytest
from django.test import TestCase
from django.urls import reverse
from mixer.backend.django import mixer
from rest_framework.test import APIClient
from wheater.models import Wheater


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

    def test_wheater_view_with_date_param(self):
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
        response = self.client.get(path + '?date=2019-06-11')
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

    def test_wheater_view_with_city_param(self):
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
        response = self.client.get(path + '?city=Chicago')
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

    def test_wheater_view_with_city_and_date_param(self):
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
        response = self.client.get(path + '?city=Chicago&date=2019-06-11')
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

    def test_wheater_view_with_sort_ordering_by_date_asc(self):
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
        mixer.blend(
            Wheater,
            date="2020-06-11",
            lat=41.8818,
            lon=-87.6231,
            city="Curitiba",
            state="Paraná",
            temperatures=[24.0, 21.5, 24.0, 19.5, 25.5]
        )
        response = self.client.get(path + '?sort=date')
        first_date = {"date": "2019-06-11"}
        second_date = {"date": "2020-06-11"}

        assert response.status_code == 200
        assert response.json()[0]["date"] == first_date["date"]
        assert response.json()[1]["date"] == second_date["date"]

    def test_wheater_view_with_sort_ordering_by_date_desc(self):
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
        mixer.blend(
            Wheater,
            date="2020-06-11",
            lat=41.8818,
            lon=-87.6231,
            city="Curitiba",
            state="Paraná",
            temperatures=[24.0, 21.5, 24.0, 19.5, 25.5]
        )
        response = self.client.get(path + '?sort=-date')
        last_date = {"date": "2020-06-11"}
        first_date = {"date": "2019-06-11"}

        assert response.status_code == 200
        assert response.json()[0]["date"] == last_date["date"]
        assert response.json()[1]["date"] == first_date["date"]

    def test_wheater_view_post(self):
        path = reverse('wheater')
        wheater = {
            "date": "2019-06-11",
            "lat": 41.8818,
            "lon": -87.6231,
            "city": "Chicago",
            "state": "Illinois",
            "temperatures": 25.5
        }
        response = self.client.post(path, data=wheater)
        response_data = {
            "id": 1,
            "date": "2019-06-11",
            "lat": 41.8818,
            "lon": -87.6231,
            "city": "Chicago",
            "state": "Illinois",
            "temperatures": 25.5
        }
        assert response.status_code == 201
        assert response.json() == response_data

@pytest.mark.django_db
class TestWheaterView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_wheaterbyid_view(self):
        path = reverse('wheaterbyid', kwargs={'pk': 1})
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
        assert response.json() == response_data
