from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)

# driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("01/01/2024")

year = "2024"
month = "January"
date = "30"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click()

Title = driver.title
while True:
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yea = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    if mon == month and yea == year:
        break
    else:
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
        driver.find_element(
            By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-w']"
        ).click()


dates = driver.find_elements(
    By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a"
)

for ele in dates:
    if ele.text == date:
        ele.click()
        break


time.sleep(5)
