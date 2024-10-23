import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
location=os.getcwd()  #current working directory


# def chrome_setup():
#     from selenium.webdriver.chrome.service import Service
#     serv_obj=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
#     #download files in desired location
#     preferences={"download.default_directory":location}
#     ops=webdriver.ChromeOptions()
#     ops.add_experimental_option("prefs",preferences)
#     driver=webdriver.Chrome(service=serv_obj,options=ops)
#     return driver
def edge_setup():
    from selenium.webdriver.edge.service import Service
    serv_obj=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
    #download files in desired location
    download_dir={"download.default_directory":location}
    ops=webdriver.EdgeOptions()
    ops.add_experimental_option("prefs",download_dir)
    driver=webdriver.Edge(service=serv_obj,options=ops)
    return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
    #settings
    ops=webdriver.FirefoxOptions()
    ops.set_preference("brouser.helperApps")
    driver=webdriver.Firefox(service=serv_obj)
    return driver

# driver=chrome_setup()
# driver=edge_setup()
driver=firefox_setup()
driver.get("https://www.learningcontainer.com/sample-mp3-file-download/")
driver.maximize_window()
driver.find_element(By.XPATH,"//div[@class='elementor-element elementor-element-c882db9 elementor-widget elementor-widget-text-editor']//div[2]//div[1]//div[1]//div[1]//div[3]//a[1]").click()
time.sleep(5)
driver.quit()