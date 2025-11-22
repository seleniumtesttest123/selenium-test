import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://jqueryui.com/"

driver = webdriver.Edge()
driver.get(url)
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
print(f"Total links: {len(links)}")

for link in links:
    href = link.get_attribute("href")
    response = requests.get(href)
    if response.status_code >= 400:
        print(f"Broken link: {href}(Status code: {response.status_code})")

driver.quit()
