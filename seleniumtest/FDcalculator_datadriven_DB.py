from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import mysql.connector
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)

driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html?classic=true"
)
driver.find_element(By.XPATH, "//*[@id='wzrk-cancel']").click()
driver.maximize_window()
try:
    con = mysql.connector.connect(
        host="localhost", port=3306, user="root", passwd="root", database="seleniumtest"
    )
    curs = con.cursor()
    curs.execute("select * from fdcalculator")
    for row in curs:
        principal = row[0]
        rateofinterest = row[1]
        period1 = row[2]
        period2 = row[3]
        frequency = row[4]
        expected = row[5]

        driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principal)
        driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(
            rateofinterest
        )
        driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)
        perioddrp = Select(
            driver.find_element(By.XPATH, "//select[@id='tenurePeriod']")
        )
        perioddrp.select_by_visible_text(period2)
        frequencydrp = Select(
            driver.find_element(By.XPATH, "//select[@id='frequency']")
        )
        frequencydrp.select_by_visible_text(frequency)
        driver.find_element(
            By.XPATH,
            "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']",
        ).click()
        actual = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

        if float(expected) == float(actual):
            print("seleniumtest passed")

        else:
            print("seleniumtest failed")

        driver.find_element(By.XPATH, "//img[@class='PL5']").click()
        time.sleep(5)
    con.close()
except:
    print("connection unsuccessful...")

driver.close()
