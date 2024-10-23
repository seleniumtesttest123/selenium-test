from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time

serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)

window_ids=driver.window_handles

# pareentwindowid=window_ids[0]
# childwindowid=window_ids[1]
# print(pareentwindowid,childwindowid)
# time.sleep(5)
#
# driver.switch_to.window(childwindowid)
# print("child:",driver.title)
#
# driver.switch_to.window(pareentwindowid)
# print("parent:",driver.title)

#approach2
# for winid in window_ids:
#     driver.switch_to.window(winid)
#     print(driver.title)

#close for a specific browsers window
for winid in window_ids:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM":
        driver.close()

time.sleep(5)