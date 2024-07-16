import pyautogui
import time

LOGS = "logs.txt"


def steam_opener():
    is_checking = True

    try:
        x, y = pyautogui.locateCenterOnScreen('D:\\Projects\\Python\\Projects\\I_Am_Lazy\\steam.png', confidence=0.9)
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.leftClick()

    except pyautogui.ImageNotFoundException:
        with open(LOGS, "w") as file:
            file.write("Couldn't find steam icon")

    while is_checking:

        try:
            x, y = pyautogui.locateCenterOnScreen('D:\\Projects\\Python\\Projects\\I_Am_Lazy\\steam_library.png', confidence=0.9)
            pyautogui.moveTo(x, y, duration=1)
            pyautogui.leftClick()
            is_checking = False

        except pyautogui.ImageNotFoundException:
            with open(LOGS, "w") as file:
                file.write("Couldn't find Library option, trying again.")
            time.sleep(5)


def opera_opener():
    try:
        x, y = pyautogui.locateCenterOnScreen('D:\\Projects\\Python\\Projects\\I_Am_Lazy\\opera.png', confidence=0.9)
        pyautogui.moveTo(x, y, duration=1)
        pyautogui.leftClick()

    except pyautogui.ImageNotFoundException:
        with open(LOGS, "w") as file:
            file.write("Couldn't find Opera icon")


steam_opener()
opera_opener()
