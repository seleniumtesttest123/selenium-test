from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@role='combobox']").click()
country = driver.find_elements(By.XPATH, "//ul[@class='select2-results__options']//li")
print(len(country))
for c in country:
    if c.text == "India":
        c.click()
        break
time.sleep(5)
driver.quit()
