import pyautogui
from time import sleep

for i in range(0,4):    
    pyautogui.typewrite('Hello world!',interval=0.25)
    pyautogui.press('enter')



