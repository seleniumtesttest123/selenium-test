import time
from selenium import webdriver

viewports = [(768, 1024), (1024, 768), (1280, 720), (414, 896)]
driver = webdriver.Edge()
driver.get("https://www.google.com")

try:
    for width, height in viewports:
        driver.set_window_size(width, height)
        time.sleep(5)
        print(f"Viewed port: {width}x{height}")

finally:
    driver.close()
