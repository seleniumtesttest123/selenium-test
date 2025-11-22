from selenium.webdriver.common.by import By
import time

from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(15)
driver.find_element(
    By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']"
).send_keys("selenium")
driver.find_element(By.XPATH, "//input[@type='submit']").click()
driver.find_element(By.LINK_TEXT, "Selenium").click()
driver.find_element(By.LINK_TEXT, "Selenium in biology").click()
driver.find_element(By.LINK_TEXT, "Selenium (software)").click()
driver.find_element(By.LINK_TEXT, "Selenium disulfide").click()
driver.find_element(By.LINK_TEXT, "Selenium dioxide").click()

windowids = driver.window_handles

for winid in windowids:
    driver.switch_to.window(winid)
    print(driver.title)
    if (
        driver.title == "Selenium - Wikipedia"
        or driver.title == "Selenium disulfide - Wikipedia"
    ):
        driver.close()
time.sleep(15)


driver.quit()
