import serial
import time
import pyautogui

ArduinoSerial = serial.Serial('COM3',9600)
time.sleep(2)

while 1:
    incoming = str (ArduinoSerial.readline()) 
    print( incoming)
    

    if 'back' in incoming:
        pyautogui.press('right') 

    if 'Vup' in incoming:
        pyautogui.hotkey('ctrl', 'up')
        
    if 'Vdn' in incoming:
        pyautogui.hotkey('ctrl', 'down')

    if 'next' in incoming:
        pyautogui.press('left')

    incoming = "";
    