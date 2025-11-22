from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class DemoMouseHover:
    def demo_mouse_events(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/")
        time.sleep(3)
        driver.maximize_window()
        achains = ActionChains(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, "//p[normalize-space()='Support']").click()
        move_button = driver.find_element(
            By.XPATH, "//p[@class='MuiTypography-root MuiTypography-body1 css-1co872k']"
        )
        time.sleep(3)
        achains.move_to_element(move_button).click().perform()
        time.sleep(5)


demo = DemoMouseHover()
demo.demo_mouse_events()
