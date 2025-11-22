from selenium.webdriver.common.by import By
import time
from selenium import webdriver

driver = webdriver.Edge()

driver.get("https://www.youtube.com/")
driver.maximize_window()
# driver.find_element(By.XPATH,"//*[@id='button']/yt-icon/yt-icon-shape/icon-shape/div").click()
# driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").click()
driver.find_element(
    By.XPATH,
    "/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input",
).send_keys("bmw")
driver.find_element(
    By.XPATH, "//*[@id='search-icon-legacy']/yt-icon/yt-icon-shape/icon-shape/div"
).click()
acttitle = driver.title
print(acttitle)
links = driver.find_elements(By.TAG_NAME, "a")
print(len(links))
time.sleep(5)
driver.close()
