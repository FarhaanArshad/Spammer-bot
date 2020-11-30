import pyautogui
import time
time.sleep(10)
text = open("rick",'r')
for word in text:
    pyautogui.typewrite(word)
    pyautogui.press('enter')