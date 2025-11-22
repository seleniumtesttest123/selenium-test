import time
from selenium.webdriver.common.by import By
from selenium import webdriver

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoWebElementState:
    def locate_web_element_state(self):
        driver = webdriver.Edge()
        driver.get("https://training.openspan.com/login")
        demo_state = driver.find_element(
            By.XPATH, "//*[@id='login_button']"
        ).is_enabled()
        print(demo_state)
        driver.find_element(By.XPATH, "//input[@id='user_name']").send_keys("test")
        driver.find_element(By.XPATH, "//input[@id='user_pass']").send_keys("test123")
        demo_state1 = driver.find_element(
            By.XPATH, "//*[@id='login_button']"
        ).is_enabled()
        print(demo_state1)
        time.sleep(5)


find_get_text = DemoWebElementState()
find_get_text.locate_web_element_state()
