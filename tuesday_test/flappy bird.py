from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

driver = webdriver.Edge(
    service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
)
driver.implicitly_wait(10)
act = ActionChains(driver)

driver.get("http://localhost/seleniumtest/")
driver.maximize_window()
time.sleep(2)
driver.find_element(
    By.XPATH, "//a[normalize-space()='html-css-javascript-..>']"
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//a[normalize-space()='19-Flappy-Bird-Game/']").click()
time.sleep(2)
hi = driver.find_element(By.ID, "myCanvas")
print("text:", hi.get_property())

time.sleep(2)
