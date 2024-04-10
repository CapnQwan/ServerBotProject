import subprocess
import pyautogui
import time

def openInstance(instance):
  shortcut_target = r'"C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance ' + instance.currentInstance.InstanceName
  subprocess.Popen(shortcut_target, shell=True)
  time.sleep(20)
  pyautogui.hotkey('win', 'up')