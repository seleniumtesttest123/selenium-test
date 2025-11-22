from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)
act = ActionChains(driver)
driver.get("https://text-compare.com")
driver.maximize_window()

text_box1 = driver.find_element(By.XPATH, "//textarea[@id='inputText1']")
text_box2 = driver.find_element(By.XPATH, "//textarea[@id='inputText2']")

text_box1.send_keys("welcome to selenium")

# CTRL+A
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()
act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# CTRL+C
act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# tab
act.key_down(Keys.TAB).key_up(Keys.TAB).perform()

# CTRL+V
act.key_down(Keys.CONTROL).send_keys("v").key_down(Keys.CONTROL).perform()

time.sleep(5)
