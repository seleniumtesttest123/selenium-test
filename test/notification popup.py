from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj,options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(5)
