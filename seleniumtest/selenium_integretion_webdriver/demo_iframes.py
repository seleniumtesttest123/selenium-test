from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DemoIframes:
    def demo_iframes(self):
        driver = webdriver.Edge()
        driver.get(
            "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css"
        )
        time.sleep(3)
        driver.maximize_window()
        # switching with iframe locator
        driver.switch_to.frame(driver.find_element(By.XPATH, "//*[@id='iframeResult']"))
        # driver.switch_to.frame("iframeResult")  # switching with name
        # driver.switch_to.frame("iframeResult")  # switching with id
        # switching with index
        driver.switch_to.frame(0)
        demo_text = driver.find_element(By.XPATH, "//a[@id='navbtn_tutorials']").click()
        print(demo_text)
        time.sleep(3)


demo = DemoIframes()
demo.demo_iframes()
