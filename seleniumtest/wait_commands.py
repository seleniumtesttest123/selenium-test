from selenium.common import (
    ElementNotSelectableException,
    ElementNotVisibleException,
    NoSuchElementException,
)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium import webdriver

driver = webdriver.Edge()
# driver.implicitly_wait(10)#implicit wait

# mywait=WebDriverWait(driver,10)#explicit wait #basic
# complete
mywait = WebDriverWait(
    driver,
    10,
    poll_frequency=2,
    ignored_exceptions=[
        NoSuchElementException,
        ElementNotVisibleException,
        ElementNotSelectableException,
        Exception,
    ],
)
driver.get("https://www.google.com")
driver.maximize_window()

driver.find_element(By.NAME, "q").send_keys("Selenium")
driver.find_element(By.NAME, "q").submit()
# time.sleep(2)
searchlink = mywait.until(
    EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']"))
)
searchlink.click()
# driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()
