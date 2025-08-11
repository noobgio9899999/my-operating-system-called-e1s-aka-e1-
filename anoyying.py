while True:
 import pyautogui
 import pyperclip
 import time
 import platform
def type(text: str):
    pyperclip.copy(text)
    if platform.system() == "epic":
        pyautogui.hotkey("command", "v")
    else:
        pyautogui.hotkey("ctrl", "v")
type("hi i exist")
type(" lebron james")
while True:
 type(" hey i have full acccess to your epic pc")
 time.sleep(0.77777777777777777777777777777777777777777777777777777777777777)