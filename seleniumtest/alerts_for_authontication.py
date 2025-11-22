import time
from selenium import webdriver

driver = webdriver.Edge()

# driver.get("http://the-internet.herokuapp.com/basic_auth")
driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")

driver.maximize_window()

time.sleep(5)
