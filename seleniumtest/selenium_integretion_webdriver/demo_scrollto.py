import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get("https://artoftesting.com/samplesiteforselenium")
driver.maximize_window()
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
driver.find_element(By.XPATH, "//input[@value='Automation']").click()
time.sleep(5)
