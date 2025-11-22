import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))


class DemoIsDisplayed:
    def locate_is_displayed(self):
        driver = webdriver.Edge()
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        element = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(element)
        time.sleep(5)
        driver.find_element(
            By.XPATH, "//button[normalize-space()='Toggle Hide and Show']"
        ).click()
        time.sleep(5)
        element1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(element1)
        time.sleep(5)

    def demo_is_displayed(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/hotels")
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@class='SearchPanel_roomDetails__jjS6x']//img[@alt='Location Icon of hotels AND cities']",
        ).click()
        time.sleep(2)
        driver.find_element(
            By.XPATH,
            "//div[@class='SelectRoom_selectorGroup__mWhJB']//div[2]//button[2]",
        ).click()
        time.sleep(2)
        element2 = driver.find_element(
            By.XPATH,
            "//div[@class='SelectRoom_selectorWrapper__OLC0A']//div[@class='SelectRoom_radioButtons__mXa0q']",
        ).is_displayed()
        print(element2)
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[normalize-space()='0']").click()
        time.sleep(2)
        element3 = driver.find_element(
            By.XPATH,
            "//div[@class='SelectRoom_selectorWrapper__OLC0A']//div[@class='SelectRoom_radioButtons__mXa0q']",
        ).is_displayed()
        print(element3)
        time.sleep(5)


find_get_text = DemoIsDisplayed()
# find_get_text.locate_is_displayed()
find_get_text.demo_is_displayed()
