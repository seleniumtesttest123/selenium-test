"""some info regarding pytest
Amazon Product Search Test

This module contains tests for searching products on Amazon.in
Snake Case: function_name
Camel Case: functionName
PascalCase (UpperCamelCase): FunctionName
Single Underscore Prefix (_variable): Private Variable
Double Underscore Prefix (__variable): Name Mangling
Single Underscore (_): Non-public variable or method
Double Underscore (__): Name Mangling
ex:
class TestClass:
    def __init__(self):
        self.public = "Anyone can access"  # Public
        self._internal = "Don't touch"     # Protected (by convention)
        self.__mangled = "Harder to find"  # Name-mangled (pseudo-private)
Double Underscore Suffix (variable__): Avoids name clashes with special methods
dunder (Double UNDERscore) Methods: __init__, __str__, __repr__
Test-Specific Conventions
Test Files: test_*.py or *_test.py
Test Functions: test_*()
Test Classes: Test*
Fixtures: @pytest.fixture def db_connection():
Markers: @pytest.mark.slow_test
-k stands for method name execution, ex: pytest -k "search"
-v stands for verbose, ex: pytest -v (stands for more info metadata)
-s stands for no capture, ex: pytest -s (logs in output)
can run specific file with py.test <filename>
-m stands for marker, ex: pytest -m "slow_test" (runs only tests with @pytest.mark.slow_test)
can skip tests with @pytest.mark.skip
expect failure with @pytest.mark.xfail
fixtures are used as setup and teardown methods for test cases and conftest.py is used for generalization of fixtures
when you define fixture scope class only, it will run once before class is initiated and once after class is terminated
when you define fixture scope function only, it will run once before function is initiated and once after function is terminated
when you define fixture scope module only, it will run once before module is initiated and once after module is terminated and it is the default scope
when you define fixture scope session only, it will run once before session is initiated and once after session is terminated
when you define fixture scope package only, it will run once before package is initiated and once after package is terminated
when you define fixture scope test only, it will run once before test is initiated and once after test is terminated
datadrivern and parametrization can be done with return statements in format like [(1,2,3), (4,5,6)] which is a list of tuples
"""

import logging
from typing import Tuple, List
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure logging
log_file = "test_amazon.log"

# Clear previous log file if it exists
open(log_file, "w").close()

# Configure root logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create file handler
file_handler = logging.FileHandler(log_file, encoding="utf-8")
file_handler.setLevel(logging.INFO)

# Create console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

logger.info("Logging initialized")

# Test data - each tuple contains (search_term, min_expected_results)
SEARCH_TERMS: List[Tuple[str, int]] = [
    ("laptops", 5),
    ("smartphones", 5),
    ("headphones", 3),
    ("books", 2),
]

# Constants
AMAZON_URL = "https://www.amazon.in/"
SEARCH_BOX_XPATH = "//input[@id='twotabsearchtextbox']"
PRODUCT_CARD_XPATH = """
    //div[contains(@class, 's-result-item')]
    [.//h2[contains(@class, 'a-size-')]]
    [.//span[contains(@class, 'a-price')]]
""".strip()

# Test data - each tuple contains (search_term, min_expected_results)
SEARCH_TERMS = [("laptops", 5), ("smartphones", 5), ("headphones", 3), ("books", 2)]


def setup_browser() -> WebDriver:
    """Initialize and configure the WebDriver."""
    logger.info("Initializing WebDriver")
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")

    driver = webdriver.Edge(options=options)
    driver.implicitly_wait(10)
    return driver


# Fixture to initialize and close the browser
@pytest.fixture(scope="module")
def browser():
    driver = setup_browser()
    yield driver
    logger.info("Quitting browser")
    driver.quit()


# Fixture for WebDriverWait
@pytest.fixture(scope="module")
def wait(browser: WebDriver) -> WebDriverWait:
    return WebDriverWait(browser, timeout=10, poll_frequency=0.5)


def search_products(driver: WebDriver, search_term: str) -> None:
    """Search for products on Amazon."""
    logger.info("Navigating to Amazon")
    driver.get(AMAZON_URL)

    logger.info(f"Searching for: {search_term}")
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, SEARCH_BOX_XPATH))
    )
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.submit()


def get_product_details(product: WebElement) -> Tuple[str, str]:
    """Extract and return product title and price."""
    title = product.find_element(
        By.XPATH, ".//h2[contains(@class, 'a-size-')]"
    ).text.strip()

    price = product.find_element(
        By.XPATH, ".//span[contains(@class, 'a-price')]//span[@class='a-offscreen']"
    ).get_attribute("textContent")

    return title, price


@pytest.mark.parametrize("search_term,min_expected_results", SEARCH_TERMS)
def test_search_products(
    browser: WebDriver, wait: WebDriverWait, search_term: str, min_expected_results: int
) -> None:
    """
    Test searching for different products on Amazon and verifying results.

    Args:
        browser: WebDriver instance
        wait: WebDriverWait instance
        search_term: Product to search for
        min_expected_results: Minimum number of expected search results
    """
    logger.info(f"Starting test for search term: {search_term}")

    try:
        # Search for products
        search_products(browser, search_term)

        # Wait for search results and verify count
        logger.debug("Waiting for search results")
        products = wait.until(
            EC.presence_of_all_elements_located((By.XPATH, PRODUCT_CARD_XPATH))
        )

        assert len(products) >= min_expected_results, (
            f"Expected at least {min_expected_results} products for '{search_term}', "
            f"but found {len(products)}"
        )

        logger.info(f"Found {len(products)} products for '{search_term}'")

        # Test first 3 products
        for i, product in enumerate(products[:3], 1):
            try:
                title, price = get_product_details(product)

                # Verify data is present and valid
                assert title, f"Product {i} title is empty"
                assert price, f"Product {i} price is empty"
                assert "₹" in price, f"Product {i} price should contain Rupee symbol"

                # Log product info
                short_title = f"{title[:47]}..." if len(title) > 50 else title
                logger.info(f"Product {i}: {short_title} - {price}")

            except Exception as e:
                logger.error(f"Error processing product {i}: {str(e)}")
                raise

        logger.info(
            f"Successfully verified {min(3, len(products))} products for '{search_term}'"
        )

    except Exception as e:
        logger.error(f"Test failed for '{search_term}': {str(e)}")
        # Take screenshot on failure
        browser.save_screenshot(f"test_failure_{search_term}.png")
        raise


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 1, 3),
        (5, 2, 10),
        (0, 5, 0),
        (-1, -1, 1),
    ],
)
def test_multiplication(a: int, b: int, expected: int) -> None:
    """Test multiplication of two numbers.

    Args:
        a: First number
        b: Second number
        expected: Expected result of a * b
    """
    logger.debug(f"Testing {a} * {b} = {expected}")
    assert a * b == expected, f"{a} * {b} should be {expected}"


def test_error_handling() -> None:
    """Test error handling with pytest.raises."""
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        _ = 1 / 0

    with pytest.raises(ValueError):
        int("not_a_number")


if __name__ == "__main__":
    # This allows running the test directly with python -m pytest test_amazon_search.py -v -s
    pytest.main(["-v", "-s", __file__])
