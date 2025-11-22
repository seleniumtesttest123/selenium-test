from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class DemoMultipleWindows:
    def demo_multiple_windows(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/")
        time.sleep(3)
        driver.maximize_window()
        parent_window = driver.current_window_handle
        print(parent_window)
        driver.find_element(
            By.XPATH,
            "//a[@title='Swiggy Instamart']//img[@alt='Swiggy Instamart Banner']",
        ).click()
        time.sleep(3)
        all_handles = driver.window_handles
        print(all_handles)
        for handle in all_handles:
            if handle != parent_window:
                driver.switch_to.window(handle)
                text = driver.find_element(
                    By.XPATH, "//img[@aria-label='Listing items for collection Yatra']"
                ).get_attribute("alt")
                print(text)
                time.sleep(3)
                child_window = driver.current_window_handle
                print(child_window)
                driver.find_element(
                    By.XPATH, "//div[@class='_3nYJY _2kXJC']//a[1]//img[1]"
                ).click()
                time.sleep(3)
                all_handles = driver.window_handles
                print(all_handles)
                for handle_cw in all_handles:
                    if handle_cw != child_window and handle_cw != parent_window:
                        driver.switch_to.window(handle_cw)
                        time.sleep(3)
                        driver.find_element(
                            By.XPATH,
                            "//a[@href='/store/apps/developer?id=Swiggy']//span[contains(text(),'Swiggy')]",
                        ).click()
                        time.sleep(3)
                        driver.close()
                        time.sleep(3)
                        break
                driver.switch_to.window(child_window)
                time.sleep(3)
                driver.close()
                time.sleep(3)
                break

        driver.switch_to.window(parent_window)
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//a[@title='Swiggy Instamart']//img[@alt='Swiggy Instamart Banner']",
        ).click()
        time.sleep(5)
        driver.quit()


dd_window = DemoMultipleWindows()
dd_window.demo_multiple_windows()
