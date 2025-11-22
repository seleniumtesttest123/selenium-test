from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Set the path to the ChromeDriver executable
service = Service(executable_path="C:/Webdrivers/edgedriver_win64/msedgedriver.exe")

# Initialize the Chrome webdriver with the service
driver = webdriver.Edge(service=service)

# Navigate to the website
driver.get("http://www.plode.org")

time.sleep(2)

# Wait for the Plode logo image to be present
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/img')
    )
)

time.sleep(2)

# Click on the Plode logo image
plode = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[1]/div[2]/div[3]/div[1]/div[1]/img'
)
plode.click()

time.sleep(2)

# Wait for the Google sign-in button to be present
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="google-signin"]/div/div'))
)

time.sleep(2)

# Click on the Google sign-in button
google = driver.find_element(By.XPATH, '//*[@id="google-signin"]/div/div')
google.click()

time.sleep(2)

# Switch to the popup window
popup_window = driver.window_handles[-1]
driver.switch_to.window(popup_window)

# Wait for the email input field to be present
input_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, ".whsOnd.zHQkBf"))
)

time.sleep(2)

# Enter the email address and press Enter
input_element.clear()
input_element.send_keys("seleniumtesttest123@gmail.com" + Keys.ENTER)

time.sleep(2)

# Wait for the password input field to be present
password_element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.NAME, "Passwd"))
)

WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, "Passwd")))
# Enter the password and press Enter
password_element.send_keys("seleniumtest@123" + Keys.ENTER)
time.sleep(2)

# Switch back to the main window
driver.switch_to.window(driver.window_handles[0])

# Wait for the "Skip" button to be present
skip_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "DeviceSelect_Skip_Button__1yP0C"))
)

# Click the "Skip" button
skip_button.click()

time.sleep(2)

# Wait for the "Yes" button to be present
yes_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "DialogModal_btn__3KPtU"))
)
# Click the "Yes" button
yes_button.click()

# Wait for the "code" element to be present
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="Selection_code__3fJWM"]/div/div/p')
    )
)
# Click on the "code" element
code = driver.find_element(By.XPATH, '//*[@id="Selection_code__3fJWM"]/div/div/p')
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="Selection_code__3fJWM"]/div/div/p'))
)
code.click()

time.sleep(2)

# Wait for the "project_based" element to be present
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located(
        (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/a/div/div/p')
    )
)
# Click on the "project_based" element
project_based = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[1]/a/div/div/p'
)
project_based.click()

time.sleep(2)

new_project = driver.find_element(By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div')
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div'))
)
new_project.click()

time.sleep(2)

teeth_led_1 = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/img[1]'
)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div[2]/div/div[3]/img[1]')
    )
)
teeth_led_1.click()

time.sleep(2)

select_internal_next = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[3]/img'
)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[2]/div[3]/div/div[3]/img')
    )
)
select_internal_next.click()

time.sleep(2)

# Scroll the browser window to the left
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.LEFT)

time.sleep(2)

wait = WebDriverWait(driver, 10)
coverflow_element = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, f"//div[@id='coverflowElement' and @cardid='22']")
    )
)

# Click on the element
coverflow_element.click()

time.sleep(2)

select_external_next = driver.find_element(
    By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div/div[3]/img'
)
WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div/div[3]/img')
    )
)
select_external_next.click()

time.sleep(2)


wait = WebDriverWait(driver, 10)
source_element = wait.until(
    EC.presence_of_element_located(
        (
            By.XPATH,
            '//*[@id="assemblyscreenid"]/div[1]/div/div[1]/div[1]/div/div/div/div/img',
        )
    )
)

# Find the target element
target_element = driver.find_element(By.XPATH, "//*[@id='PC_dragSource']")

# Get the location of the target element
target_location = target_element.location

# Calculate the offset to drop the source element to the left of the target element
horizontal_offset = target_location["x"] - 50  # Adjust this value as needed
vertical_offset = target_location["y"]

# Perform drag-and-drop operation by offset
action_chains = ActionChains(driver)
action_chains.drag_and_drop_by_offset(
    source_element, horizontal_offset, vertical_offset
).perform()

time.sleep(2)


# Wait for some time for demonstration purposes
time.sleep(10)

# Close the browser
driver.quit()
