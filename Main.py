from tkinter import *
from tkinter import ttk
from Server import Server
from InstanceManager import InstanceManager
import threading

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
SERVER.BindIntanceManager(InstanceManager())

thread = threading.Thread(target=SERVER.WaitForConnection)
thread.daemon = True
thread.start()

thread = threading.Thread(target=SERVER.HandleClient)
thread.daemon = True
thread.start()

APP.mainloop()
