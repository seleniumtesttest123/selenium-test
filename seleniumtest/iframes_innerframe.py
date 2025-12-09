from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(
    By.XPATH, "//a[normalize-space()='Iframe with in an Iframe']"
).click()
outerframe = driver.find_element(By.XPATH, "//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe = driver.find_element(
    By.XPATH, "/html[1]/body[1]/section[1]/div[1]/div[1]/iframe[1]"
)
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")

# switch to parent frame
# driver.switch_to.parent_frame()

time.sleep(5)


# driver.switch_to.default_content()
# driver.switch_to.parent_frame()