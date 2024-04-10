import pyautogui

def openMonopoly(instance):
  image_location = pyautogui.locateOnScreen('./Images/MonopolyGoIcon.PNG', confidence=0.8)
  if image_location:
    pyautogui.click(image_location)
    state = 'initilize'