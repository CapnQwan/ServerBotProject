from .Instance_Handlers import * 
from .Instance import Instance

class InstanceManager():
  activeState = 'paused'
  currentInstance = None
  def __init__(self):
    pass
  def setInstance(self, instance = 0): 
    self.currentInstance = Instance(instance)

  def handleMessage(self, message):
    if self.currentInstance == None:
      self.setInstance()
    variables = message.split(' ')
    function = variables.pop(0)

    if function == 'openInstance':
      openInstance(self)
    if function == 'openApp':
      openMonopoly(self)

