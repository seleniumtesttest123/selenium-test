from main import get_wether


def test_get_weather():
    assert get_wether(19) == "cold"
    assert get_wether(22) == "hot"
