import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoSeleniumLearning:
    def demo_browser_methods(self):
        driver = webdriver.Edge()
        driver.get("https://training.rcvacademy.com")
        print(driver.current_url)
        print(driver.title)
        driver.maximize_window()
        driver.fullscreen_window()
        driver.refresh()
        driver.find_element(By.LINK_TEXT, "ALL COURSES").click()
        time.sleep(2)
        driver.back()
        time.sleep(2)
        driver.forward()
        time.sleep(2)
        driver.minimize_window()
        time.sleep(5)
        driver.quit()


demobrowser = DemoSeleniumLearning()
demobrowser.demo_browser_methods()
