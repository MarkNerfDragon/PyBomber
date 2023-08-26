import pyautogui, time
time.sleep(0.1); f = open("scripttext.txt", "r")
for line in f:
	pyautogui.typewrite(line)
	pyautogui.press("enter")
