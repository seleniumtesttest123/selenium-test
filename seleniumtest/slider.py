from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Edge(
    service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
)
driver.implicitly_wait(10)
act = ActionChains(driver)
driver.get("https://jqueryui.com/resources/demos/slider/range.html")
driver.maximize_window()

min = driver.find_element(By.XPATH, "//span[1]")
max = driver.find_element(By.XPATH, "//span[2]")
print(f"before moving  min : {min.location}  max : {max.location}  ")

act.drag_and_drop_by_offset(min, 100, 0).perform()
act.drag_and_drop_by_offset(max, -50, 0).perform()
print(f"after moving  min : {min.location}  max : {max.location}  ")

time.sleep(5)



# slider = driver.find_element(By.XPATH, "//span[1]")
# act.click_and_hold(slider).move_by_offset(100, 0).release().perform()
