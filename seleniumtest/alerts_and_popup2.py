from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
# opens alert window
driver.find_element(By.XPATH, "//input[@value='Login']").click()

time.sleep(5)

driver.switch_to.alert.accept()

time.sleep(5)
