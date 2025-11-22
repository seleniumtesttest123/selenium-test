from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

# Get the absolute path to the HTML file
html_path = os.path.abspath(
    "C:/Users/vinay/Documents/Flappy Bird/index.html"
)  # Make sure this is the correct filename

# Setup the WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Edge(
    service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
)
driver.implicitly_wait(10)
options = webdriver.EdgeOptions()
options.add_argument(
    "--allow-file-access-from-files"
)  # This is needed to run local files
# driver = webdriver.Chrome(options=options)  # Or use Firefox(), Safari(), etc.

try:
    # Load the local HTML file
    driver.get(f"file:///{html_path}")

    # Wait for the canvas to be present
    canvas = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "canvas"))
    )

    # Inject JavaScript to expose game state
    driver.execute_script(
        """
        window.getBirdInfo = function() {
            if (typeof bird !== 'undefined' && typeof game_mode !== 'undefined') {
                return {
                    y: bird.y,
                    velocity: bird.velocity_y,
                    gameMode: game_mode
                };
            }
            return null;
        };
    """
    )

    # Start the game
    ActionChains(driver).move_to_element(canvas).click().perform()

    last_y = None
    while True:
        # Get bird info
        bird_info = driver.execute_script("return window.getBirdInfo();")

        if bird_info is None:
            print("Game variables not found. Make sure the game has started.")
            time.sleep(1)
            continue

        current_y = bird_info["y"]
        velocity = bird_info["velocity"]
        game_mode = bird_info["gameMode"]

        # Check bird motion
        if last_y is not None:
            if current_y > last_y:
                print("Bird is falling")
            elif current_y < last_y:
                print("Bird is rising")
            else:
                print("Bird is stationary")

        # Check for collision
        if game_mode == "over":
            print("Bird hit an obstacle! Game over.")
            break

        last_y = current_y

        # Optional: make the bird jump periodically
        if current_y > 200:  # Adjust this threshold as needed
            ActionChains(driver).move_to_element(canvas).click().perform()

        time.sleep(0.1)  # Adjust the interval as needed

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
