from selenium.webdriver.common.by import By

import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()
time.sleep(2)
# opens alert window
driver.find_element(
    By.XPATH, "//button[normalize-space()='Click for JS Prompt']"
).click()

time.sleep(2)

alertwindow = driver.switch_to.alert
print(alertwindow.text)
alertwindow.send_keys("welcome")
alertwindow.accept()  # close the alert window using ok button
# alertwindow.dismiss()
time.sleep(5)
