# need to install the package requests from prefrence interpreter
import requests as requests
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

alllinks = driver.find_elements(By.TAG_NAME, "a")
count = 0
for link in alllinks:
    url = link.get_attribute("href")
    try:
        res = requests.head(url)
    except:
        None

    res = requests.head(url)
    if res.status_code >= 400:
        print(url, "is broken link")
        count += 1
    else:
        print(url, "is a valid link")
print("Total number 0 fbroken links: ", count)
