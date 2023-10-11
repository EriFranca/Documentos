import pyautogui
import time

pyautogui.alert("Alerta")
pyautogui.PAUSE = 0.5
pyautogui.press('winleft')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write("https://guiadosquadrinhos.com.br")
pyautogui.press('enter')
#teste