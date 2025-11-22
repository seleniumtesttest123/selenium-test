from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import XLUtils
import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true"
)
driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()
driver.maximize_window()


file = "C:\\Users\\vinay\\OneDrive\\Documents\\hi.xlsx"
rows = XLUtils.getRowCount(file, "Sheet1")

for r in range(2, rows + 1):
    principal = XLUtils.readData(file, "Sheet1", r, 1)
    rateofinterest = XLUtils.readData(file, "Sheet1", r, 2)
    period1 = XLUtils.readData(file, "Sheet1", r, 3)
    period2 = XLUtils.readData(file, "Sheet1", r, 4)
    frequency = XLUtils.readData(file, "Sheet1", r, 5)
    expected = XLUtils.readData(file, "Sheet1", r, 6)

    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principal)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofinterest)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)
    perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    perioddrp.select_by_visible_text(period2)
    frequencydrp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydrp.select_by_visible_text(frequency)
    driver.find_element(
        By.XPATH,
        "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']",
    ).click()
    actual = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    if float(expected) == float(actual):
        print("seleniumtest passed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Passed")
        XLUtils.fillGreenColor(file, "Sheet1", r, 8)
    else:
        print("seleniumtest failed")
        XLUtils.writeData(file, "Sheet1", r, 8, "Failed")
        XLUtils.fillRedColor(file, "Sheet1", r, 8)

    driver.find_element(By.XPATH, "//img[@class='PL5']").click()


time.sleep(5)
driver.quit()
