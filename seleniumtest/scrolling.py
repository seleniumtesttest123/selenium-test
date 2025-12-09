from selenium import webdriver
import time

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# scroll by pixel
# driver.execute_script("window.scrollBy(0,3000)","")  # scrollTo also works the same as scrollBy
# value=driver.execute_script("return window.pageYOffset;")
# print("Number o pixels moved:",value)

# scroll down page till the element is visible
# gender=driver.find_element(By.XPATH,"//label[normalize-space()='Gender:']")
# driver.execute_script("arguments[0].scrollIntoView();",gender)
# value=driver.execute_script("return window.pageYOffset;")
# print("Number o pixels moved:",value)

# scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)
time.sleep(2)
# scroll to starting
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)

time.sleep(5)
