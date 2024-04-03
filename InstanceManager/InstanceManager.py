from .Instance import Instance
import subprocess

class InstanceManager():
  activeState = 'paused'
  currentInstance = None
  def __init__(self):
    pass
  def setInstance(self, instance = 0): 
    self.currentInstance = Instance(instance)
  def openInstance(self,):
    if self.currentInstance == None:
      self.setInstance()
    shortcut_target = r'"C:\Program Files\BlueStacks_nxt\HD-Player.exe" --instance ' + self.currentInstance.InstanceName
    subprocess.Popen(shortcut_target, shell=True)
  def handleMessage(self, message):
    variables = message.split(' ')
    function = variables.pop(0)
    if function == 'openInstance':
      self.openInstance()

