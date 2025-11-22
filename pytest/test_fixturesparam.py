import pytest


@pytest.fixture(scope="module", params=["www.google.com", "www.amazon.com"])
def val(request):
    return request.param


def test_val(val):
    assert val != None
