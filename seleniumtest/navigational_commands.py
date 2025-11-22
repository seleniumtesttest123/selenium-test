import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https:www.snapdeal.com")
time.sleep(2)
driver.get("https:www.amazon.com")
time.sleep(2)

driver.back()
print(driver.current_url)
time.sleep(2)
driver.forward()
print(driver.current_url)
time.sleep(2)
driver.refresh()
print(driver.current_url)
time.sleep(2)
driver.quit()
