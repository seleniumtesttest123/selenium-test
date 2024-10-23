from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT,"Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()
#find the no of links for all the links in the page
#links=driver.find_elements(By.XPATH,'//a'
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))
#print all the links
for link in links:
     print(link.text)
time.sleep(5)