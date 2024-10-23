#need to install the package requests from prefrencec interpreter
import requests as requests
from selenium import webdriver
from selenium.common import ElementNotSelectableException, ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks=driver.find_elements(By.TAG_NAME,'a')
count=0
for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None

    res=requests.head(url)
    if res.status_code>=400:
        print(url,"is broken link")
        count+=1
    else:
        print(url,"is a valid link")
print("Total number 0 fbroken links: ",count)
