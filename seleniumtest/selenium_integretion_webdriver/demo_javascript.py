from selenium import webdriver
import time


class DemoJs:
    def demo_javascript(self):
        driver = webdriver.Edge()
        # driver.get("https://training.rcvacademy.com/")
        driver.execute_script(
            "window.open('https://training.rcvacademy.com/courses', '_self');"
        )
        time.sleep(2)
        demo_element = driver.execute_script(
            "return document.getElementsByTagName('p')[1];"
        )
        driver.execute_script("arguments[0].click();", demo_element)

        driver.maximize_window()
        time.sleep(5)


demojs = DemoJs()
demojs.demo_javascript()
