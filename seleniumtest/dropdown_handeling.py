from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

# drop=driver.find_element(By.XPATH,"//div[@class='VfPpkd-aPP78e']")
dropd = Select(driver.find_element(By.XPATH, "//select[@id='yearbox']"))

# dropd.select_by_visible_text("2000")
# dropd.select_by_value("2000")
# dropd.select_by_index(85)
dropdowncount = driver.find_elements(By.XPATH, "//select[@id='yearbox']//option")
print(len(dropdowncount))
# capture all the options and print them
countoptions = dropd.options
print("total no of options:", len(countoptions))

# for opt in countoptions:
#    print(opt.text)

# select  option from dropdown without using built_in methods
# for opt in countoptions:
#    if opt.text=="2000":
#        opt.click()
#        break

time.sleep(5)
