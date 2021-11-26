# El paso 1 es grabar lo que se controla en pantalla
# Sacado de https://www.geeksforgeeks.org/create-a-screen-recorder-using-python/

import random
import pyautogui
import time
import os

zonas = {
    "menu": {
        "archivo": {
            "coords": {"x1": 32, "y1": 3, "x2": 105, "y2": 33},
            "nuevo_archivo": {
                "coords": {"x1": 41, "y1": 36, "x2": 41 + 338, "y2": 36 + 40}
            },
        }
    }
}


def main():
    os.system("Code")
    time.sleep(3)
    pyautogui.hotkey("winleft", "up", "up")
    time.sleep(1)
    pyautogui.hotkey("ctrl", "+", "+")
    time.sleep(3)
    pyautogui.hotkey("ctrl", "num0")
    pyautogui.hotkey("alt", "F4")

    # os.startfile("C:/Users/BLJ/AppData/Local/Programs/Microsoft VS Code/Code.exe")
    # time.sleep(7)

    # pyautogui.hotkey("alt", "a")
    # time.sleep(1)
    # pyautogui.typewrite(["up", "up", "up", "up", "enter"], 1)
    # time.sleep(4)
    # pyautogui.click()
    # time.sleep(4)
    # pyautogui.typewrite(["window.moveTo(100, 10);", "enter"], 1)
    # https://www.w3schools.com/jsref/met_win_moveto.asp

    screenWidth, screenHeight = pyautogui.size()
    # Returns two integers, the x and y of the mouse cursor's current position.
    currentMouseX, currentMouseY = pyautogui.position()
    # Move the mouse to the x, y coordinates 100, 150.
    # pyautogui.moveTo(*punto(4, "menu", "archivo"))
    # pyautogui.click()
    # pyautogui.moveTo(*punto(4, "menu", "archivo", "nuevo_archivo"))
    # pyautogui.click()


def punto(tiempo, *camino):

    global zonas
    tmp = zonas[camino[0]]
    for i in range(1, len(camino)):
        tmp = tmp[camino[i]]
    tmp = tmp["coords"]
    a, b, c = (
        random.randrange(tmp["x1"], tmp["x2"]),
        random.randrange(tmp["y1"], tmp["y2"]),
        tiempo,
    )
    print(a, b, c)
    return (a, b, 4)


def prueba():
    # Returns two integers, the width and height of the screen. (The primary monitor, in multi-monitor setups.)
    screenWidth, screenHeight = pyautogui.size()
    # Returns two integers, the x and y of the mouse cursor's current position.
    currentMouseX, currentMouseY = pyautogui.position()
    # Move the mouse to the x, y coordinates 100, 150.
    pyautogui.moveTo(100, 150)
    # Click the mouse at its current location.
    pyautogui.click()
    # Click the mouse at the x, y coordinates 200, 220.
    pyautogui.click(200, 220)
    # Move mouse 10 pixels down, that is, move the mouse relative to its current position.
    pyautogui.move(None, 10)
    # Double click the mouse at the
    pyautogui.doubleClick()
    # Use tweening/easing function to move mouse over 2 seconds.
    pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)
    # Type with quarter-second pause in between each key.
    pyautogui.write("Hello world!", interval=0.25)
    # Simulate pressing the Escape key.
    pyautogui.press("esc")
    pyautogui.keyDown("shift")
    pyautogui.write(["left", "left", "left", "left", "left", "left"])
    pyautogui.keyUp("shift")
    pyautogui.hotkey("ctrl", "c")


if __name__ == "__main__":
    main()
