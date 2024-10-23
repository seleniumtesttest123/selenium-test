from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Edge(service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe"))
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

act=ActionChains(driver)
# act.move_to_element(admin).move_to_element(usermanagement).move_to_element(users).click().perform()
driver.find_element(By.XPATH,"//input[@id='product_549']").click()
driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
Indonesia=driver.find_element(By.XPATH,"//span[@class='select2-results']//ul/li")

country=driver.find_elements(By.XPATH,"//span[@class='select2-results']//ul/li")
for i in country:
    # print(i.text)

    if "Indonesia" in i.text:
        # i.click()

        act.move_to_element(i).click().perform()
        break





time.sleep(15)
driver.quit()