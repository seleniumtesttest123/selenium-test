import pytest


@pytest.fixture(
    scope="session", autouse=True
)  # scope=function/class/module/package/session and autouse for the fixtures for all the tests
def setUp(browser):
    if browser == "chrome":
        print("launch chrome")
    elif browser == "ff":
        print("launch firefox")
    else:
        print("provide valid browser")
    print("login")
    print("browse products")
    yield
    print("logoff")
    print("close browser")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="session", autouse=True)
def browser(request):
    return request.config.getoption("--browser")


# pytest -v -s --browser chrome
