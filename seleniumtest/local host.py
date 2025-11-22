from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

driver = webdriver.Edge()
driver.implicitly_wait(10)
act = ActionChains(driver)

driver.get("http://localhost/seleniumtest")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//a[normalize-space()='tuesday-js-master/'] ").click()
time.sleep(2)
driver.find_element(By.XPATH, "//td[contains(text(),'Quick tutorial')]").click()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("Number of pixels moved:", value)
email = driver.find_element(
    By.XPATH, "//td[contains(text(),'tuesdayjsengine@gmail.com')]"
)
print("Contact info: ", email.text)
time.sleep(2)
window_ids = driver.window_handles
for winid in window_ids:
    driver.switch_to.window(winid)
    if (
        driver.title
        == "Tuesday JS visual novel engine Tutorial / Documentation / Lessons"
    ):
        time.sleep(2)
        driver.find_element(
            By.XPATH, "//div[contains(text(),'Quick tutorial')]"
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[contains(text(),'User interface')]"
        ).click()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[contains(text(),'Project structure')]"
        ).click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[contains(text(),'Add-on')]").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[contains(text(),'Lessons')]").click()
        time.sleep(1)
        act.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        driver.find_element(
            By.XPATH, "//div[contains(text(),'Android Version')]"
        ).click()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        act.key_down(Keys.ARROW_UP).key_up(Keys.ARROW_UP).perform()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[normalize-space()='English']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//div[@id='doc_view']").click()
        time.sleep(2)
        driver.close()


time.sleep(5)
driver.quit()
