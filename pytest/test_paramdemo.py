import pytest

# @pytest.fixture(params=["a", "b"])  # for usernames and password
# def demo_fixture(request):
#     print(request.param)
# def testAdd(demo_fixture):
#     print("login successful")


@pytest.mark.parametrize("a, b, final", [(2, 6, 8), (5, 8, 15), (5, 10, 15)])
def testAdd(a, b, final):
    assert a + b == final


# def testLogoff():
#     print("logoff successful")
#
#
# def testCalculation():
#     assert 2 + 2 == 5
