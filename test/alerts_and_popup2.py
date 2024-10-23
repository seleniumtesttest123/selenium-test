from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://mypage.rediff.com/login/dologin")
driver.maximize_window()
#opens alert window
driver.find_element(By.XPATH,"//input[@value='Login']").click()

time.sleep(5)

driver.switch_to.alert.accept()

time.sleep(5)
