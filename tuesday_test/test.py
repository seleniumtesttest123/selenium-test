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

driver.get("https://gitlab.com/test2874825/hi.git")
driver.maximize_window()
time.sleep(200)
driver.find_element(By.XPATH, "//*[@id='qquD4']/div/label/input").click
time.sleep(2)
