from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from datetime import datetime


class DemoScreenshot:
    def demo_screenshot(self):

        driver = webdriver.Edge()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(3)
        driver.maximize_window()
        cont_demo = driver.find_element(By.XPATH, "//button[@id='login-continue-btn']")
        cont_demo.screenshot(".\\test.png")  # to save in the current directory
        cont_demo.click()
        time.sleep(2)
        driver.get_screenshot_as_file(
            "C:\\Users\\vinay\\PycharmProjects\\pythonProject\\seleniumtest\\selenium_integretion_webdriver\\error.png"
        )  # png is recommended
        driver.save_screenshot(".\\test1.png")
        time.sleep(5)


ddscreenshot = DemoScreenshot()
ddscreenshot.demo_screenshot()
