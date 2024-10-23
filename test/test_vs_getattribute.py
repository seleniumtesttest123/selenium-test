from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://admin-demo.nopcommerce.com/login")

emailbox=driver.find_element(By.XPATH,"//input[@id='Email']")
emailbox.clear()
emailbox.send_keys("abc@gmail.com")

print("result of text:",emailbox.text)#returns innertext
print("result of get_attribute():",emailbox.get_attribute('value'))#returns value of any attribute of the web element.

button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("text:",button.text)
print("get_attribute:",button.get_attribute('value'))
print("get_attribute:",button.get_attribute('type'))
time.sleep(2)