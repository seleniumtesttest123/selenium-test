from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# count the no of rows and colums
noofrows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr"))
noofcolums = len(
    driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]//th")
)

print(noofrows)
print(noofcolums)
# specific data in rowand the column
# data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data)

# printing all the data in the no of rows and colums
print("printing all the data in the table")

# for r in range(2,noofrows+1):
#     for c in range(1,noofcolums+1):
#         data = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end='            ')
#     print()
# Read data based on condition()
for r in range(2, noofrows + 1):
    authName = driver.find_element(
        By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]"
    ).text
    if authName == "Mukesh":
        bookname = driver.find_element(
            By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]"
        ).text
        price = driver.find_element(
            By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]"
        ).text
        print(bookname, "          ", authName, "         ", price)

time.sleep(5)
driver.close()
