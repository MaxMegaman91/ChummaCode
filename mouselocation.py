import pyautogui, time

index = 0
while index < 500:
    time.sleep(0.25)
    print(pyautogui.position())
    index +=1
