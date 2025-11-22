from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.by import By


class DemoExplicitWait:
    def demo_explicit_wait(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/")
        # wait = WebDriverWait(driver, 10)
        wait = WebDriverWait(
            driver, 10, 2, ignored_exceptions=[ElementClickInterceptedException]
        )
        driver.maximize_window()
        wait.until(
            Ec.element_to_be_clickable(
                (By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']")
            )
        ).click()
        wait.until(
            Ec.element_to_be_clickable(
                (By.XPATH, "//input[@id='input-with-icon-adornment']")
            )
        ).send_keys("New Delhi")
        depart_from = wait.until(
            Ec.element_to_be_clickable(
                (By.XPATH, "//input[@id='input-with-icon-adornment']")
            )
        )

        depart_from.send_keys("New Delhi")

        depart_from.send_keys(Keys.TAB)

        wait.until(
            Ec.element_to_be_clickable(
                driver.find_element(By.XPATH, "//div[@class='css-36ryd3']")
            )
        ).click()


dd = DemoExplicitWait()
dd.demo_explicit_wait()
