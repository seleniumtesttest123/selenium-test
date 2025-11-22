from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time

driver = webdriver.Edge(
    service=Service("C:/Webdrivers/edgedriver_win64/msedgedriver.exe")
)

driver.get(
    "file:///C:/wamp64/www/seleniumtest/html-css-javascript-games-main/19-Flappy-Bird-Game/index.html"
)
time.sleep(2)


def get_game_mode():
    return driver.execute_script("return game_mode;")


def get_score():
    return driver.execute_script(
        """
        var score = 0;
        for (var i = 0; i < pipes.length; i++)
            if (pipes[i].x < bird.x) score = score + 0.5;
        return Math.floor(score);
    """
    )


def has_collided():
    return driver.execute_script(
        """
        for (var i = 0; i < pipes.length; i++)
            if (ImagesTouching(bird, pipes[i])) return true;
        return false;
    """
    )


def reset_game_directly():
    try:
        driver.execute_script(
            "game_mode = 'running'; bird.y = myCanvas.height / 2; bird.angle = 0; pipes = []; add_all_my_pipes();"
        )
        print("Game state reset directly.")
    except Exception as e:
        print(f"Error resetting game state directly: {e}")


def verify_scoring():
    initial_score = get_score()
    jumps = 0
    max_jumps = 50

    while get_game_mode() == "running" and jumps < max_jumps:
        action.click().perform()
        jumps += 1
        time.sleep(0.49)

        current_score = get_score()
        if current_score > initial_score:
            print(f"Score increased to {current_score}")
            initial_score = current_score

    print(f"Final score after scoring test: {current_score}")


# Function to seleniumtest edge cases
def test_edge_cases():
    # Test collision with the top edge
    driver.execute_script("bird.y = 0; bird.velocity_y = -10;")
    time.sleep(1)
    assert get_game_mode() == "over", "Game did not end after top edge collision"
    print("Game ended after collision with the top edge.")
    reset_game_directly()
    driver.execute_script(
        "bird.y = myCanvas.height - bird.MyImg.height; bird.velocity_y = 10;"
    )
    time.sleep(1)
    assert get_game_mode() == "over", "Game did not end after bottom edge collision"
    print("Game ended after collision with the bottom edge.")


action = ActionChains(driver)
action.click().perform()

WebDriverWait(driver, 10).until(lambda d: get_game_mode() == "running")

initial_score = get_score()
jumps = 0
max_jumps = 50  # Limit the number of jumps to avoid infinite loop

while get_game_mode() == "running" and jumps < max_jumps:
    action.click().perform()
    jumps += 1
    time.sleep(0.49)  # Wait a bit between jumps

    current_score = get_score()
    if current_score > initial_score:
        print(f"Score increased to {current_score}")
        initial_score = current_score

    if has_collided():
        print("Bird has collided with a pipe")
        break

assert get_game_mode() == "over", "Game did not end as expected"

final_score = get_score()
print(f"Final score: {final_score}")

print("Performing reset through JavaScript...")
reset_game_directly()

print("Verifying scoring mechanism...")
verify_scoring()

print("Testing edge cases...")
test_edge_cases()

print("All tests passed successfully!")
driver.quit()
