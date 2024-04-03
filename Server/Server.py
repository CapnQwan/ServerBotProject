import socket

class Server():
  ConnectionStatus = False
  InstanceManager = None
  connectionStatusLabel = None
  def __init__(self, Address=('', 5000), MaxClient=1, connectionStatusLabel=None):
    self.socket = socket.socket()
    self.socket.bind(Address)
    self.socket.listen(MaxClient)
    self.connectionStatusLabel = connectionStatusLabel
  def WaitForConnection(self):
    while True:
      self.Client, self.Adr=(self.socket.accept())
      if self.connectionStatusLabel:
        self.connectionStatusLabel.config(text='Got a connection from: '+str(self.Client)+'.')
        self.ConnectionStatus = True
  def HandleClient(self):
    while True:
      # Handle client's requests here
      # For simplicity, let's just print received messages
      if not self.ConnectionStatus:
        continue
      try:
        message = self.Client.recv(1024).decode('utf-8')
        if not message:
          break  # If client disconnected, break the loop
        if self.InstanceManager is not None:
          self.InstanceManager.handleMessage(message)
      except ConnectionResetError:
        print("Client disconnected.")
        self.ConnectionStatus = False
        if self.connectionStatusLabel:
          self.connectionStatusLabel.config(text='Client disconnected.')
        break
  def BindIntanceManager(self, InstanceManager):
    self.InstanceManager = InstanceManager