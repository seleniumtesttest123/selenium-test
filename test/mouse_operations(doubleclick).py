from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Edge(service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe"))
driver.implicitly_wait(10)
act=ActionChains(driver)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame("iframeResult")

field1=driver.find_element(By.XPATH,"//input[@id='field1']")
field1.clear()
field1.send_keys("welcome")

button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
act.double_click(button).perform()
time.sleep(5)