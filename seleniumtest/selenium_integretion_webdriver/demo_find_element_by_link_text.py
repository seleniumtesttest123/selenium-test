import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoElementLocatorsByLinkText:
    def locate_by_link_demo(self):
        driver = webdriver.Edge()
        driver.get("https://www.bbc.com/news")
        driver.maximize_window()
        time.sleep(15)
        driver.find_element(By.LINK_TEXT, "Live").click()
        time.sleep(5)


findbyid = DemoElementLocatorsByLinkText()
findbyid.locate_by_link_demo()
