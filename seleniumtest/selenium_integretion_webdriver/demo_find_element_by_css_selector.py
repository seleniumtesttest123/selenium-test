import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoElementLocatorsByCssSelector:
    def locate_by_css_demo(self):
        driver = webdriver.Edge()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.CSS_SELECTOR, "#login-input").send_keys("test@test.com")
        time.sleep(5)


findbyid = DemoElementLocatorsByCssSelector()
findbyid.locate_by_css_demo()
