import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoGetAttribute:
    def locate_get_attribute(self):
        driver = webdriver.Edge()
        driver.get("https://yatra.com")
        attributevalue = driver.find_element(
            By.XPATH, "//button[normalize-space()='Search']"
        ).get_attribute("type")
        print(attributevalue)
        time.sleep(5)


find_get_text = DemoGetAttribute()
find_get_text.locate_get_attribute()
