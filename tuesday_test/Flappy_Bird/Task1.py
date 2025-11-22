from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

driver = webdriver.Edge(
    service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
)
driver.implicitly_wait(10)

driver.get(
    "file:///C:/wamp64/www/seleniumtest/html-css-javascript-games-main/19-Flappy-Bird-Game/index.html"
)
time.sleep(2)

canvas = driver.find_element(By.ID, "myCanvas")
driver.execute_script("game_mode = 'running';")
start_time = time.time()
canvas.screenshot("before_collision.png")
while True:
    elapsed_time = time.time() - start_time
    if elapsed_time > 28:
        break
    driver.execute_script("Got_Player_Input(new Event('keydown'));")
    time.sleep(0.493)

canvas.screenshot("after_collision.png")
time.sleep(3)


try:
    game_mode = driver.execute_script("return game_mode;")
    if game_mode == "over":
        print("Collision detected and Game Over screen displayed correctly.")
    else:
        print(
            f"Failed to detect collision or Game Over screen. Current game mode: {game_mode}"
        )
except Exception as e:
    print(f"Failed to retrieve game mode. Error: {str(e)}")

driver.quit()
