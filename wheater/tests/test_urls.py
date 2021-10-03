from django.urls import reverse, resolve
from django.urls.conf import path


class TestUrls:
    def test_detail_urls(self):
        path = reverse('wheater')
        assert resolve(path).view_name == 'wheater'

    def test_detail_urls(self):
        path = reverse('wheaterbyid', kwargs={'pk': 1})
        assert resolve(path).view_name == 'wheaterbyid'