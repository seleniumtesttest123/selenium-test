from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class DemoSliderHandle:
    def demo_slider(self):
        driver = webdriver.Edge()
        driver.get("https://www.snapdeal.com/products/mobiles-accessories?sort=plrty")
        time.sleep(3)
        driver.maximize_window()
        time.sleep(3)
        element1 = driver.find_element(By.XPATH, "//a[contains(@class, 'left-handle')]")
        element2 = driver.find_element(
            By.XPATH, "//a[contains(@class, 'right-handle')]"
        )
        ActionChains(driver).drag_and_drop_by_offset(element1, 60, 0).perform()
        time.sleep(
            3
        )  # synchronisation is important while using drag and drop as it takes time to load
        # ActionChains(driver).click_and_hold(element1).move_by_offset(50, 0).release().perform()
        # ActionChains(driver).move_to_element(element2).pause(1).click_and_hold(element2).move_by_offset(-80, 0).release().perform()
        ActionChains(driver).drag_and_drop_by_offset(element2, -80, 0).perform()
        time.sleep(3)


ds = DemoSliderHandle()
ds.demo_slider()
