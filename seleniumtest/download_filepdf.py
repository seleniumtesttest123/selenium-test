import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()  # current working directory


def chrome_setup():
    # download files in desired location
    preferences = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True,
    }
    ops = webdriver.ChromeOptions()
    ops.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(options=ops)
    return driver


def edge_setup():
    # download files in desired location
    download_dir = {
        "download.default_directory": location,
        "plugins.always_open_pdf_externally": True,
    }
    ops = webdriver.EdgeOptions()
    ops.add_experimental_option("prefs", download_dir)
    driver = webdriver.Edge(options=ops)
    return driver


def firefox_setup():
    # settings
    ops = webdriver.FirefoxOptions()
    ops.set_preference(
        "browser.helperApps.neverAsk.saveToDisk", "application/pdf"
    )  # link for Mime types https://www.sitepoint.com/mime-types-complete-list/
    ops.set_preference("browser.download.manager.showWhenStarting", False)
    ops.set_preference(
        "browser.download.folderList", 2
    )  # 0=desktop,1=download,2=desired location
    ops.set_preference("browser.download.dir", location)
    ops.set_preference("pdfjs.disabled", True)
    driver = webdriver.Firefox(options=ops)
    return driver


# driver=chrome_setup()
driver = edge_setup()
# driver=firefox_setup()
driver.get("https://www.learningcontainer.com/sample-mp3-file-download/")
driver.maximize_window()
driver.find_element(
    By.XPATH,
    "//div[@class='elementor-element elementor-element-c882db9 elementor-widget elementor-widget-text-editor']//div[2]//div[1]//div[1]//div[1]//div[3]//a[1]",
).click()
time.sleep(5)
driver.quit()
