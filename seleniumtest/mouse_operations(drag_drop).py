from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)
act = ActionChains(driver)
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

rome = driver.find_element(By.ID, "box6")
italy = driver.find_element(By.ID, "box106")
act.drag_and_drop(rome, italy).perform()

oslo = driver.find_element(By.ID, "box1")
norway = driver.find_element(By.ID, "box101")
act.drag_and_drop(oslo, norway).perform()
time.sleep(5)
