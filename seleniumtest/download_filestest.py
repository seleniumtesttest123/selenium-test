from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# Specify the download directory
location = os.getcwd()
download_dir = location  # Replace with your desired download path

# Configure Edge options
edge_options = webdriver.EdgeOptions()
edge_options.add_experimental_option(
    "prefs",
    {
        "download.default_directory": download_dir,
        "download.prompt_for_download": False,
        "directory_upgrade": True,
        "safebrowsing.enabled": True,
    },
)

# Initialize the webdriver with options
driver = webdriver.Edge(options=edge_options)
driver.implicitly_wait(10)

try:
    # Open the URL
    driver.get("https://www.learningcontainer.com/sample-doc-file/")
    driver.maximize_window()

    # Click the download link for the desired file
    download_link = driver.find_element(By.XPATH, "//a[contains(@href, 'sample.doc')]")
    download_link.click()

    # Wait for the download to complete (adjust time as necessary)
    time.sleep(20)

    # Check if the file has been downloaded
    file_path = os.path.join(
        download_dir, "sample.doc"
    )  # Adjust the file name based on the actual downloaded file
    if os.path.exists(file_path):
        print(f"File downloaded successfully: {file_path}")
    else:
        print("File not found.")
finally:
    # Clean up and close the browser
    driver.quit()
