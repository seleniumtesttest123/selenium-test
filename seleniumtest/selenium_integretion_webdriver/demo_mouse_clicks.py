from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class DemoRightDoubleClick:
    def demo_right_double_click(self):
        driver = webdriver.Edge()
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        time.sleep(3)
        driver.maximize_window()
        right_click = driver.find_element(
            By.XPATH, "//span[@class='context-menu-one btn btn-neutral']"
        )
        double_click = driver.find_element(
            By.XPATH, "//button[normalize-space()='Double-Click Me To See Alert']"
        )
        achains = ActionChains(driver)
        time.sleep(3)
        achains.context_click(right_click).perform()  # right click
        time.sleep(3)
        achains.double_click(double_click).perform()  # double click
        time.sleep(3)
        driver.quit()


demo = DemoRightDoubleClick()
demo.demo_right_double_click()
