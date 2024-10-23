from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/register")
driver.maximize_window()

#is_displayed and is_enabled
#searchbox=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
#print("Display status:",searchbox.is_displayed())
#print("Enabled status:",searchbox.is_enabled())


#is_selected
radio_male=driver.find_element(By.XPATH,"//input[@id='gender-male']")
radio_female=driver.find_element(By.XPATH,"//input[@id='gender-female']")

print("Default radiobutton status.....")
print(radio_male.is_selected())
print(radio_female.is_selected())

radio_male.click()

print("After selecting male radio button.....")
print(radio_male.is_selected())
print(radio_female.is_selected())

radio_female.click()

print("After selecting female radio button.....")
print(radio_male.is_selected())
print(radio_female.is_selected())

time.sleep(2)
driver.quit()