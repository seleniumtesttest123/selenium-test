from selenium import webdriver
from selenium.webdriver.edge.service import Service
import time

ops = webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

serv_obj = Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver = webdriver.Edge(service=serv_obj, options=ops)

driver.get("https://whatmylocation.com/")
driver.maximize_window()

time.sleep(5)
