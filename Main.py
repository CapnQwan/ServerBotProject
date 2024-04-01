from tkinter import *
from tkinter import ttk
import socket
import threading

class Server():
  def __init__(self,Adress=('',5000),MaxClient=1):
      self.s = socket.socket()
      self.s.bind(Adress)
      self.s.listen(MaxClient)
  def WaitForConnection(self):
      print('Waiting for connection')
      self.Client, self.Adr=(self.s.accept())
      connectionString = 'Got a connection from: '+str(self.Client)+'.'

class App(Tk):
   def __init__(self):
      super().__init__()

WINDOW_TABS = ['Main', 'Stats', 'Debug']
connectionString = 'waiting for connection...'

app = App()
nb = ttk.Notebook(app)

frame1 = Frame(nb, width=500, height=350)

label1 = ttk.Label(frame1, text = connectionString)
label1.pack(pady = 50, padx = 20)

frame1.pack()


nb.add(frame1)

nb.pack(padx = 0, pady = 0, expand = True)


s = Server()

thread = threading.Thread(target=s.WaitForConnection)
thread.daemon = True
thread.start()

app.mainloop()
