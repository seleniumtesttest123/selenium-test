from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='product_549']").click()
driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("TestT")
driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Test")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='dob']").click()
drop_month = Select(
    driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
)
drop_month.select_by_visible_text("Apr")
drop_month = Select(
    driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
)
drop_month.select_by_visible_text("2024")
dates = driver.find_elements(
    By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a"
)
for d in dates:
    if d.text == "20":
        d.click()
        break
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='sex_1']").click()
# driver.find_element(By.XPATH,"//input[@id='addmorepax']").click()
# driver.find_element(By.XPATH,"//span[@id='select2-addpaxno-container']").click()
# driver.find_element(By.XPATH,"//input[@role='combobox']").send_keys("add 1 more passenger (100%)"+ Keys.ENTER)
# driver.find_element(By.XPATH,"//input[@id='travname2']").send_keys("Test2T")
# driver.find_element(By.XPATH,"//input[@id='travlastname2']").send_keys("Test2")
driver.find_element(By.XPATH, "//input[@id='traveltype_1']").click()
driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Dharwad")
driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Nepal")
time.sleep(2)

driver.find_element(By.XPATH, "//input[@id='departon']").click()
ddrop_month = Select(
    driver.find_element(By.XPATH, "//select[@aria-label='Select month']")
)
ddrop_month.select_by_visible_text("Jun")
ddrop_year = Select(
    driver.find_element(By.XPATH, "//select[@aria-label='Select year']")
)
ddrop_year.select_by_visible_text("2025")
ddates = driver.find_elements(
    By.XPATH, "//div[@id='ui-datepicker-div']//table/tbody/tr/td/a"
)
for dd in ddates:
    if dd.text == "5":
        dd.click()
        break
time.sleep(2)

driver.find_element(
    By.XPATH, "//span[@aria-label='State / District / Province']"
).click()


time.sleep(5)
