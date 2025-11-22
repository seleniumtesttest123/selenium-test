import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoRadioButtons:
    def demo_radio_buttons(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/")
        time.sleep(5)
        driver.maximize_window()
        var1 = driver.find_element(By.XPATH, "//input[@value='2']").is_selected()
        print(var1)
        driver.find_element(By.XPATH, "//input[@value='2']").click()
        time.sleep(5)
        var2 = driver.find_element(By.XPATH, "//input[@value='2']").is_selected()
        print(var2)
        time.sleep(5)


find_get_text = DemoRadioButtons()
find_get_text.demo_radio_buttons()
