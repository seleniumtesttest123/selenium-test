from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https:www.snapdeal.com")
time.sleep(2)
driver.get("https:www.amazon.com")
time.sleep(2)

driver.back()
print(driver.current_url)
time.sleep(2)
driver.forward()
print(driver.current_url)
time.sleep(2)
driver.refresh()
print(driver.current_url)
time.sleep(2)
driver.quit()

