from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://www.facebook.com/")
driver.maximize_window()

#driver.find_element(By.CSS_SELECTOR,"#email").send_keys("9448006966")#tag id

#driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("9448006966")#tag class

driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("9448006966")#tag attribute

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_pass]").send_keys("9448006966")#tag class attribute
inputelements=driver.find_elements(By.CSS_SELECTOR,".inputtext")
print(len(inputelements))
time.sleep(5)