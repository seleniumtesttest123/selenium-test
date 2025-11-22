import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://opensorce-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
time.sleep(2)
driver.close()
