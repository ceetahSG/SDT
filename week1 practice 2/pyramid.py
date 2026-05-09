import pyautogui
import time

time.sleep(5)

n = int(input())

for i in range(n):
    for j in range(i+1):
        pyautogui.typewrite("#")
    pyautogui.typewrite("\n")


