from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


class DemoDragDrop:
    def demo_drag_drop(self):
        driver = webdriver.Edge()
        driver.get("https://jqueryui.com/droppable/")
        time.sleep(3)
        driver.maximize_window()
        driver.switch_to.frame(
            driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        )
        time.sleep(3)
        drag_from = driver.find_element(By.XPATH, "//div[@id='draggable']")
        drop_to = driver.find_element(By.XPATH, "//div[@id='droppable']")
        # ActionChains(driver).drag_and_drop(drag_from, drop_to).perform()  # drag and drop
        ActionChains(driver).drag_and_drop_by_offset(drag_from, 100, 40).perform()
        time.sleep(3)


demo = DemoDragDrop()
demo.demo_drag_drop()
