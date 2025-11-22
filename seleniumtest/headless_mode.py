import time
from selenium import webdriver


def headless_chrome():
    ops = webdriver.ChromeOptions()
    ops.headless = True  # ops.add_argument("headless")
    driver = webdriver.Chrome(options=ops)
    return driver


def headless_edge():
    ops = webdriver.EdgeOptions()
    ops.add_argument(
        "headless"
    )  # Using 'ops.headless = True' may not be recognized in some versions of the Edge WebDriver.
    driver = webdriver.Edge(options=ops)

    return driver


def headless_firefox():
    ops = webdriver.FirefoxOptions()
    ops.headless = True
    driver = webdriver.Firefox(options=ops)
    return driver


# Choose the browser you want to run headlessly
# driver = headless_chrome()
driver = headless_edge()
# driver = headless_firefox()

driver.get("https://demo.nopcommerce.com/login?ReturnUrl=%2Fcustomer%2Finfo")
print(driver.title)
print(driver.current_url)
time.sleep(5)
driver.close()
