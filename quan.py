import playsound
import pyautogui
import random
import ctypes
import os

ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.dirname(__file__) + "\quanBackground.jpg" , 0)

for i in range(5):
    pyautogui.moveTo(random.randint(0,1920),random.randint(0,1080))




    


    

while True:
    pyautogui.press("volumeup",1)
    playsound.playsound(os.path.dirname(__file__)+"\quanSound.wav")
