import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoDropdownSingleSelect:
    def demo_dropdown(self):
        driver = webdriver.Edge()
        driver.get(
            "https://www.salesforce.com/au/form/signup/sales-ee/?d=topnav2-btn-ft"
        )
        time.sleep(5)
        driver.maximize_window()
        dropdown = driver.find_element(By.NAME, "CompanyCountry")
        dd = Select(dropdown)
        dd.select_by_visible_text(
            "United States"
        )  # select by visible text or name or value or index
        time.sleep(5)
        dd.select_by_index(2)  # select by index
        time.sleep(5)
        dd.select_by_value("IN")  # select by value
        time.sleep(5)


find_get_text = DemoDropdownSingleSelect()
find_get_text.demo_dropdown()
