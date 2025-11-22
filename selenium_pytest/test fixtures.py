import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options


@pytest.fixture(scope="module")
def launchbrowser():
    # driver_path = "C:/Webdrivers/edgedriver_win64/msedgedriver.exe"
    # service = Service(executable_path=driver_path)
    # edge_options = Options()
    # edge_options.add_experimental_option("detach", True)  # Keep browser open
    # edge_options.add_argument("--start-maximized")
    # driver = webdriver.Edge(service=service, options=edge_options)

    options = Options()
    options.add_experimental_option("detach", True)
    global driver
    driver = webdriver.Edge(options=options)  # Will work now!
    yield
    driver.quit()


@pytest.fixture(scope="class")
def launchbrowserclass(request):
    options = Options()
    options.add_experimental_option("detach", True)
    request.cls.driver = webdriver.Edge(options=options)
    yield
    request.cls.driver.quit()


def test_printurl(launchbrowser):
    driver.get("https://www.google.com")


def test_printurl2(launchbrowser):
    print(driver.current_url)


@pytest.mark.usefixtures("launchbrowserclass")
class Test_google:
    def test_entertheurl(self):
        self.driver.get("https://www.google.com")
