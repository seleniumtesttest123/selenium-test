import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class DemoDropdownSingleSelect:
    def demo_dropdown(self):
        driver = webdriver.Edge()
        driver.get("https://demoqa.com/select-menu")
        time.sleep(5)
        driver.maximize_window()
        dropdown = driver.find_element(By.CLASS_NAME, "CompanyCountry")
        dd = Select(dropdown)
        dd.select_by_visible_text("United States")
        time.sleep(5)
        dd.select_by_index(2)
        time.sleep(5)
        dd.select_by_value("IN")
        dd.deselect_by_visible_text("United States")
        dd.deselect_by_index(2)
        dd.deselect_by_value("IN")
        dd.deselect_all()
        time.sleep(5)


find_get_text = DemoDropdownSingleSelect()
find_get_text.demo_dropdown()

# if it's a dynamic multi select dropdown

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
#
# driver = webdriver.Chrome()
# driver.get("https://demoqa.com/select-menu")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
#
# # -----------------------------
# # SELECT COLORS
# # -----------------------------
# colors_to_select = ["Green", "Black", "Blue"]
#
# for color in colors_to_select:
#     input_box = wait.until(
#         EC.presence_of_element_located((By.ID, "react-select-4-input"))
#     )
#     input_box.send_keys(color)
#     input_box.send_keys(Keys.ENTER)
#     time.sleep(5)
#
#
# print("✅ Colors Selected:", colors_to_select)
# time.sleep(3)  # <-- Your requested pause
#
# # -----------------------------
# # DESELECT COLORS (Correct Logic)
# # Remove one at a time until none exist
# # -----------------------------
# input_box = wait.until(EC.presence_of_element_located((By.ID, "react-select-4-input")))
# input_box.click()
# time.sleep(1)
#
# while True:
#     chips = driver.find_elements(By.CSS_SELECTOR, "div[class*='multiValue']")
#     if len(chips) == 0:
#         break  # ✅ No chips → stop
#
#     input_box.send_keys(Keys.BACK_SPACE)
#     time.sleep(1)
#
#
#
# print("❌ All Colors Deselected")
# time.sleep(3)  # <-- Your requested pause
#
# driver.quit()
