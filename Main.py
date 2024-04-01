from tkinter import *
from tkinter import ttk

class App(Tk):
   def __init__(self):
      super().__init__()

WINDOW_TABS = ['Main', 'Stats', 'Debug']


app = App()
nb = ttk.Notebook(app)

frame1 = Frame(nb, width=500, height=350)

label1 = ttk.Label(frame1, text = "This is Window One")
label1.pack(pady = 50, padx = 20)

frame2 = Frame(nb, width=500, height=350)
frame1.pack()


nb.add(frame1, text = "Window 1")
nb.add(frame2, text = "Window 2")

nb.pack(padx = 0, pady = 0, expand = True)
app.mainloop()