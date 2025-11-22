from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time


class DemoImplicitWait:
    def demo_implicit_wait(self):
        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )
        driver.get("https://login.salesforce.com/?locale=au")
        driver.maximize_window()
        # driver.implicitly_wait(10)
        driver.find_element(By.XPATH, "//input[@id='username']").send_keys("test")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("test123")


dd = DemoImplicitWait()
dd.demo_implicit_wait()
