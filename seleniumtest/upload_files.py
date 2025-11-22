from selenium.webdriver.common.by import By
import time

from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get("https://tiiny.host/?content=pdf")
driver.maximize_window()

driver.find_element(
    By.XPATH,
    "//div[@id='content-selector-tabpane-pdf']//div[@class='container-dropzone tr-landing-upload-file-zone']//div//input[@type='file']",
).send_keys("C:\\Users\\vinay\\OneDrive\\Documents\\seleniumtest.pdf")


time.sleep(5)
