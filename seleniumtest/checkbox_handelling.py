from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.implicitly_wait(5)
driver.get("https://echoecho.com/htmlforms09.htm")
driver.maximize_window()

# select one specific checkbox
# driver.find_element(By.XPATH,"//td[@class='table8']//input[1]").click()

# select all the checkboxes
checkbox = driver.find_elements(
    By.XPATH, "//td//input[@type='checkbox'and contains(@name,'option')]"
)
# print(len(checkbox))
# for i in range(len(checkbox)):
#    checkbox[i].click()
# approach 2
# for checkboxs in checkbox:
#    checkboxs.click()
# select multiple checkboxes by choice
# for checkboxs in checkbox:
#    weekname=checkboxs.get_attribute('value')
#    print(weekname)
#    if weekname=='Milk' or weekname=='Cheese':
#     checkboxs.click()
# select last 2 checkboxes
# for i in range(len(checkbox)-2,len(checkbox)):
# checkbox[i].click()
# select first 2 checkboxes
# for i in range(len(checkbox)):
#    if i<2:
#        checkbox[i].click()
# clearing all the checkboxes
for checkboxs in checkbox:
    if checkboxs.is_selected():
        checkboxs.click()
time.sleep(5)
