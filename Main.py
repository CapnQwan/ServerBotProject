from tkinter import *
from tkinter import ttk
import socket
import threading

WINDOW_TABS = ['Main', 'Stats', 'Debug']

class Server():
  connectionStatusLabel = None
  def __init__(self, Address=('', 5000), MaxClient=1, connectionStatusLabel=None):
      self.socket = socket.socket()
      self.socket.bind(Address)
      self.socket.listen(MaxClient)
      self.connectionStatusLabel = connectionStatusLabel
  def WaitForConnection(self):
      self.Client, self.Adr=(self.socket.accept())
      if self.connectionStatusLabel:
        self.connectionString.config(text='Got a connection from: '+str(self.Client)+'.')

class App(Tk):
   def __init__(self):
      super().__init__()
      
APP = App()
nb = ttk.Notebook(APP)

frame1 = Frame(nb, width=500, height=350)

connectionStatus = ttk.Label(frame1, text = 'waiting for connection...')
connectionStatus.pack(pady = 50, padx = 20)

frame1.pack()


nb.add(frame1)

nb.pack(padx = 0, pady = 0, expand = True)


SERVER = Server(connectionStatusLabel=connectionStatus)

thread = threading.Thread(target=SERVER.WaitForConnection)
thread.daemon = True
thread.start()


APP.mainloop()
