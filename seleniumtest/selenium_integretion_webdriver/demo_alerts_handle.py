from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time


class Demojspopup:
    def demo_alerts(self):
        driver = webdriver.Edge()
        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        time.sleep(3)
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        # driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@id='iframeResult']"))

        # accept
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)

        # dismiss
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.dismiss()
        time.sleep(3)

        # send_keys in alert
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        driver.switch_to.alert.send_keys("w3")
        time.sleep(3)
        driver.switch_to.alert.accept()
        time.sleep(3)

        # get_text
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(3)
        print("Alert text is: ", driver.switch_to.alert.text)
        Alert(driver).accept()
        # driver.switch_to.alert.accept()
        time.sleep(3)

        driver.quit()


demo = Demojspopup()
demo.demo_alerts()
