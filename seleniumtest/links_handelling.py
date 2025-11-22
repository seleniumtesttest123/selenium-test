from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Digital downloads").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Digital").click()
# find the no of links for all the links in the page
# links=driver.find_elements(By.XPATH,'//a'
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
# print all the links
for link in links:
    print(link.text)
time.sleep(5)
