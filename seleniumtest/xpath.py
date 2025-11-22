from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time
from selenium import webdriver

driver = webdriver.Edge()
# driver.get("https://www.facebook.com")
# driver.maximize_window()
# relative or full
# driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[2]/a").click()
# partial or Xpath
# driver.find_element(By.XPATH,'//*[@id="reg_pages_msg"]/a').click()

# driver.find_element(By.XPATH,"//*[@id='email' or @class='inputtext']").send_keys("hi")

# driver.find_element(By.XPATH,"//*[contains(@id,'email')]").send_keys("9448006966")
# driver.find_element(By.XPATH,"//input[@id='pass']").send_keys("944800696645459")
# driver.find_element(By.NAME,"login").click()

# axes
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")

# self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Timken India')]/self::a").text
# print(text_msg)

# parent
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Timken India')]/parent::td").text
# print(text_msg)

# child
# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Timken India')]/ancestor::tr/child::td")
# print(len(childs))

# ancestor
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Timken India')]/ancestor::tr").text
# print(text_msg)

# desendant
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Timken India')]/ancestor::tr/descendant::*")
# print("Number of descendent nodes:",len(text_msg))

# following
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Timken India')]/ancestor::tr/following::*")
# print("Number of following nodes:",len(text_msg))

# following sibling
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Timken India')]/ancestor::tr/following-sibling::*")
# print("Number of following nodes:",len(text_msg))

# preceding
# text_msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Timken India')]/ancestor::tr/preceding::tr")
# print("Number of following nodes:",len(text_msg))

# preceding sibling
text_msg = driver.find_elements(
    By.XPATH, "//a[contains(text(),'Timken India')]/ancestor::tr/preceding-sibling::tr"
)
print("Number of following nodes:", len(text_msg))
time.sleep(2)
driver.close()
