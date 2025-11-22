import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoElementLocatorsByXPath:
    def locate_by_xpath_demo(self):
        driver = webdriver.Edge()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.XPATH, "//input[@id='login-input']").send_keys(
            "test@test.com"
        )
        time.sleep(5)


findbyid = DemoElementLocatorsByXPath()
findbyid.locate_by_xpath_demo()
