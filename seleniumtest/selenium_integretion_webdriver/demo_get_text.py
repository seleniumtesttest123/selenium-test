import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoGetText:
    def locate_get_text(self):
        driver = webdriver.Edge()
        driver.get("https://yatra.com")
        text = driver.find_element(
            By.XPATH,
            "//span[normalize-space()='Enjoy Secure Flight Bookings with Protection']",
        ).text
        print(text)
        time.sleep(5)


find_get_text = DemoGetText()
find_get_text.locate_get_text()
