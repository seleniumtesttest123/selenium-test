from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException


class ElementStable:
    def __init__(self, locator):
        self.locator = locator

    def __call__(self, driver):
        try:
            element = driver.find_element(*self.locator)
            # Wait for element to be visible and stable
            return (
                element.is_displayed()
                and element.size["width"] > 0
                and element.size["height"] > 0
            )
        except:
            return False


def wait_for_stable_elements(driver, by, value, timeout=10, check_interval=0.5):
    """Wait until no new elements are added/removed for a certain period"""
    end_time = time.time() + timeout
    last_count = 0
    stable_count = 0
    required_stable_checks = 3  # Number of consecutive stable checks to confirm

    while time.time() < end_time:
        current_count = len(driver.find_elements(by, value))
        if current_count == last_count:
            stable_count += 1
            if stable_count >= required_stable_checks:
                break
        else:
            stable_count = 0
            last_count = current_count
        time.sleep(check_interval)
    return last_count


from selenium.webdriver.support import expected_conditions as Ec
import time
import random
from datetime import datetime


class DemoAutoSuggest:
    def demo_auto_suggest(self):
        driver = webdriver.Edge()
        driver.get("https://www.yatra.com/")
        time.sleep(3)
        driver.maximize_window()
        driver.find_element(
            By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']"
        ).click()
        time.sleep(2)
        depart_from = driver.find_element(
            By.XPATH, "//input[@id='input-with-icon-adornment']"
        )
        time.sleep(2)
        depart_from.send_keys("New Delhi")
        time.sleep(2)
        depart_from.send_keys(Keys.TAB)
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='css-36ryd3']").click()
        time.sleep(2)
        # text = driver.find_element(By.XPATH, "//div[@aria-label='Departure From New Delhi inputbox']").text
        # print(text)
        driver.find_element(By.XPATH, "//p[normalize-space()='Going To']").click()
        time.sleep(2)
        going_to = driver.find_element(
            By.XPATH, "//input[@id='input-with-icon-adornment']"
        )
        time.sleep(2)
        going_to.send_keys("New")
        time.sleep(5)
        search_results = driver.find_elements(
            By.XPATH, "//*[@id='__next']//div//ul//div//li//div//div//div[1]"
        )
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York, (JFK)" in results.text:
                results.click()
                time.sleep(5)
                break

        time.sleep(4)
        # driver.find_element(By.XPATH, "//div[@class='css-w7k25o']").click()
        # time.sleep(4)
        # driver.find_element(
        #     By.XPATH, "//div[contains(@aria-label,'Choose Tuesday, July 8th, 2025')]"
        # ).click()
        # time.sleep(5)

        # Optional: Click a specific date
        target_month = "September 2025"
        target = "September 1st, 2025"
        driver.find_element(By.XPATH, "//div[@class='css-w7k25o']").click()
        time.sleep(4)
        months_visible = driver.find_elements(
            By.XPATH, "//span[@class= 'react-datepicker__current-month']"
        )
        time.sleep(4)
        for month in months_visible:
            print(month.text)
        time.sleep(4)
        for month in months_visible:
            if target_month not in month.text:
                driver.find_element(
                    By.XPATH,
                    "//button[@aria-label='Next Month'][not(@style= 'visibility: hidden;')]",
                ).click()
            else:
                print("month found")
                break
        time.sleep(10)
        dates = driver.find_elements(
            By.XPATH,
            "//div[@class='react-datepicker__month-container']//div[contains(@aria-label,'Choose')]",
        )

        # Print all aria-labels of those date divs
        for date in dates:
            label = date.get_attribute("aria-label")
            if label.startswith("Choose"):
                print(label)
        time.sleep(4)

        for date in dates:
            if target in date.get_attribute("aria-label"):
                date.click()
                break

        time.sleep(4)

        driver.find_element(By.XPATH, "//button[normalize-space()='Search']").click()
        time.sleep(30)
        driver.find_element(
            By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']"
        ).click()
        time.sleep(5)
        # Scroll to load all results with stabilization
        last_height = 0
        same_height_count = 0
        max_same_height = 3  # Number of times we'll accept the same height before considering it stable

        while same_height_count < max_same_height:
            # Scroll to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait for any dynamic content to load
            time.sleep(1.5)

            # Get new height and compare
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                same_height_count += 1
            else:
                same_height_count = 0
                last_height = new_height

            # Small scroll to trigger lazy loading if near bottom
            driver.execute_script("window.scrollBy(0, 200);")
            time.sleep(0.5)
        # Wait for elements to stabilize after scrolling
        wait = WebDriverWait(driver, 10)

        # Wait for at least one element to be present and stable
        try:
            wait.until(ElementStable((By.XPATH, "//span[@aria-label='1 Stop']")))
        except TimeoutException:
            print("No stable '1 Stop' elements found after waiting")
            return

        # Wait for the count of elements to stabilize
        wait_for_stable_elements(driver, By.XPATH, "//span[@aria-label='1 Stop']")

        # Find all visible 1 Stop elements with retry for stale elements
        attempts = 0
        max_attempts = 3
        allstops1 = []

        while attempts < max_attempts and not allstops1:
            try:
                elements = driver.find_elements(
                    By.XPATH, "//span[@aria-label='1 Stop']"
                )
                allstops1 = [el for el in elements if el.is_displayed()]
                print(
                    f"Found {len(allstops1)} visible '1 Stop' elements (attempt {attempts + 1})"
                )
            except StaleElementReferenceException:
                print(f"Stale elements found, retrying... (attempt {attempts + 1})")
                attempts += 1
                time.sleep(1)
                continue

        if not allstops1:
            print("No visible '1 Stop' elements found after retries")
            return

        if not allstops1:
            print("No visible 1 Stop elements found!")
            # Take a screenshot for debugging
            driver.save_screenshot("no_stops_found.png")
            print("Screenshot saved as 'no_stops_found.png'")
            return

        # Verify each visible element
        for i, stop in enumerate(allstops1, 1):
            try:
                stop_text = stop.text.strip()
                print(f"\nElement {i} - Text: '{stop_text}'")

                # More flexible assertion
                assert (
                    "1 stop" in stop_text.lower()
                ), f"Expected '1 stop' but found: '{stop_text}'"
                print(f"✅ Assert passed for element {i}")

            except Exception as e:
                print(f"❌ Error with element {i}:")
                print(f"Text: '{stop.text}'")
                print(f"HTML: {stop.get_attribute('outerHTML')}")
                print(f"Location: {stop.location}")
                print(f"Size: {stop.size}")
                print(f"Error: {str(e)}")
                # Take a screenshot of the element
                driver.save_screenshot(f"error_element_{i}.png")
                print(f"Screenshot saved as 'error_element_{i}.png'")
                raise
        time.sleep(5)


find_get_text = DemoAutoSuggest()
find_get_text.demo_auto_suggest()
