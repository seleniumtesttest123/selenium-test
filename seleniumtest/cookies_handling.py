import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/login?ReturnUrl=%2Fcustomer%2Finfo")
driver.maximize_window()

cookies = driver.get_cookies()
print("no of cookies: ", len(cookies))

# for c in cookies:
#     # print(c)
#     print(c.get("name"),":",c.get("value"))

# add  new cookie
driver.add_cookie({"name": "Mycookie", "value": "123456789"})
cookies = driver.get_cookies()
print("no of cookies: ", len(cookies))
# for c in cookies:
#     print(c)

# delete specific cookie
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print("no of cookies: ", len(cookies))

# delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("no of cookies: ", len(cookies))

time.sleep(5)
