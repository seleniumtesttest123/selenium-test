from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

driver=webdriver.Edge(service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe"))
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

#scroll by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value=driver.execute_script("return window.pageYOffset;")
# print("Number o pixels moved:",value)

#scroll down page till the element is visible
# gender=driver.find_element(By.XPATH,"//label[normalize-space()='Gender:']")
# driver.execute_script("arguments[0].scrollIntoView();",gender)
# value=driver.execute_script("return window.pageYOffset;")
# print("Number o pixels moved:",value)

#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number o pixels moved:",value)
time.sleep(2)
#scroll to starting
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("Number o pixels moved:",value)

time.sleep(5)