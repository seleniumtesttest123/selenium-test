import requests
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/broken_images")
driver.maximize_window()

images = driver.find_elements(By.TAG_NAME, "img")
broken_images = []
print(f"Total images: {len(images)}")

for image in images:
    src = image.get_attribute("src")
    if src:
        response = requests.get(src)
        if response.status_code != 200:
            broken_images.append(src)
            print(f"Broken image found: {src}(Status code: {response.status_code})")

if broken_images:
    print(f"\nTotal broken images: {len(broken_images)}")
    for broken_image in broken_images:
        print(broken_image)
else:
    print("\nNo broken images found")

driver.quit()
