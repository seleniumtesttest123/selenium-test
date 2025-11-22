from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from pywinauto import Desktop
from pywinauto.keyboard import send_keys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains


driver = webdriver.Edge(
    service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
)
driver.implicitly_wait(10)
act = ActionChains(driver)

driver.get("http://localhost/seleniumtest/")
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//a[normalize-space()='tuesday-js-master/']").click()

driver.find_element(By.XPATH, "//td[contains(text(),'Run in browser')]").click()

popup_window = driver.window_handles[-1]
driver.switch_to.window(popup_window)

driver.find_element(By.XPATH, "/html/body/div[6]/div/table/tbody/tr/td[2]/div").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[contains(text(),'Add story block')]").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[normalize-space()='Create block']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[@class='button_block icon icon_more']").click()
time.sleep(2)
driver.find_element(By.XPATH, "//div[@id='add_b_block_1']").click()
time.sleep(2)
driver.find_element(
    By.XPATH,
    "//body[1]/div[7]/div[1]/table[1]/tbody[1]/tr[2]/td[1]/table[1]/tbody[1]/tr[1]/td[2]",
).click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[@id='files_img']").click()
time.sleep(2)
driver.find_element(By.XPATH, "(//td[@title='delet'])[1]").click()
time.sleep(2)
original_window = driver.current_window_handle


folder_path = "C:\\Users\\vinay\\OneDrive\\Pictures\\Screenshots\\"
send_keys(folder_path)
time.sleep(5)
send_keys("{ENTER}")
time.sleep(5)
send_keys("{ENTER}")
time.sleep(10)


act.key_down(Keys.ENTER).perform()


driver.find_element(By.XPATH, "//td[@id='files_img']").click()

# driver.find_element(By.XPATH,"//input[@id='scene_class']").send_keys("test1")
# time.sleep(2)
# driver.find_element(By.XPATH,"//td[normalize-space()='Apply']").click()
time.sleep(200)

driver.quit()
