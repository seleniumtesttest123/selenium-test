from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge(service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe"))
driver.implicitly_wait(10)
act=ActionChains(driver)
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act.context_click(button).perform()
time.sleep(2)
driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
time.sleep(2)
driver.switch_to.alert.accept()


time.sleep(5)