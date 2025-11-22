import time
import os
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# driver.save_screenshot("C:\\Users\\vinay\\PycharmProjects\\pythonProject\\seleniumtest\\homepage.png")
# driver.save_screenshot(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")
# driver.get_screenshot_as_png()#saves in binary format
# driver.get_screenshot_as_base64()
time.sleep(5)
