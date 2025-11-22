import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class DemoElementsLocatorsByTag:
    def locate_by_tag_demo(self):
        driver = webdriver.Edge()
        driver.get("https://www.bbc.com/news")
        driver.maximize_window()
        time.sleep(10)
        lista = driver.find_elements(By.TAG_NAME, "input")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(5)


findbyid = DemoElementsLocatorsByTag
findbyid.locate_by_tag_demo()
