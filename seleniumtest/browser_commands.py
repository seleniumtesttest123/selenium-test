from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "OrangeHRM, Inc").click()
time.sleep(2)
driver.close()
time.sleep(2)
driver.quit()
