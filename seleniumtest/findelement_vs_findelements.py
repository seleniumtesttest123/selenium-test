from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://demo.nopcommerce.com/")
time.sleep(2)
# locator matching with single webelement
# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# element.send_keys("Apple MacBook Pro 13-inch")

# locator matching with multiple webelements
# element=driver.find_element(By.XPATH,"//div[@class='footer']//a")
# time.sleep(2)
# print(element.text)

# element not aavailable then throw nosuch element exception
# driver.find_element(By.LINK_TEXT,"Log in")
# driver.close()

# find elements
# locator matching with single element
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))
# print(elements[0].send_keys("Apple MacBook Pro 13-inch"))

# locator matching with multiple webelements
# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(elements))
# print(elements[0].text)
# for i in elements:
#    print(i.text)

# Element not available - zero
elements = driver.find_elements(By.LINK_TEXT, "Log in")
print("Elements returned:", len(elements))

time.sleep(5)
driver.quit()
