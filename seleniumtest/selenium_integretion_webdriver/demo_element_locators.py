import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoElementLocatorsByIdAndName:
    def locate_by_id_demo(self):
        driver = webdriver.Edge()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        # driver.find_element(By.ID, "login-input").send_keys("test@test.com")
        driver.find_element(By.NAME, "login-input").send_keys("test@test.com")
        time.sleep(5)


findbyid = DemoElementLocatorsByIdAndName()
findbyid.locate_by_id_demo()
