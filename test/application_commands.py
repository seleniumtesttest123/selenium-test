from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://opensorce-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
time.sleep(2)
driver.close()