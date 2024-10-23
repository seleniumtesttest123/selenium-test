from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select
import time



serv_obj =Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
driver=webdriver.Edge(service=serv_obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()

drop_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
drop_month.select_by_visible_text("Jan")

drop_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
drop_year.select_by_visible_text("2000")

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")
for d in dates:
    if d.text=="30":
        d.click()
        break
time.sleep(5)
