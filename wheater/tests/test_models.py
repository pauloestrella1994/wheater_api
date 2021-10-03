import pytest
from wheater.models import Wheater

@pytest.mark.django_db
class TestModels:
    def test_wheater_model(self):
        wheater = Wheater.objects.create(
            date = '2021-01-01',
            lat = 41.8818,
            lon = -87.6231,
            city = "Chicago",
            state = "Illinois",
            temperatures = [24.0, 21.5, 24.0, 19.5, 25.5]
        )
        assert wheater.date == '2021-01-01'
        assert wheater.lat == 41.8818
        assert wheater.lon == -87.6231
        assert wheater.city == "Chicago"
        assert wheater.state == "Illinois"
        assert wheater.temperatures == [24.0, 21.5, 24.0, 19.5, 25.5]

