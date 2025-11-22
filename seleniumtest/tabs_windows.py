from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import time
from selenium.webdriver.edge.options import Options


options = Options()
options.add_experimental_option("detach", True)
driver = webdriver.Edge(options=options)
driver.implicitly_wait(10)

# driver.get("https://demo.nopcommerce.com/login?ReturnUrl=%2Fcustomer%2Finfo")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL + Keys.RETURN)#only googlechrome

# opens a new tab and switches to new tab
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.switch_to.new_window('tab')
driver.switch_to.new_window("window")
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
time.sleep(5)
