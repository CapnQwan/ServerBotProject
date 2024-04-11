import pyautogui

def openMonopoly(instance):
  image_location = pyautogui.locateOnScreen('./Images/MonopolyGoIcon.PNG', confidence=0.8)
  print('opening monopoly')
  if image_location:
    print('icon found')
    pyautogui.click(image_location)
    state = 'initilize'