import tkinter as tk
import tkinter.messagebox
#funkcja callbackmusi przyjąć jeden parametr -obiekt opisujący zdarzenie
def klik(zdarz=None):
    tk.messagebox.showinfo(title='Klik!',message='To był klik!')
master=tk.Tk()
b1=tk.Button(master,text="b1")
b1.pack()
#metoda bind wymaga dwóch parametrów -nazwa zdarzenia i adres funkcji callback
b1.bind('<ButtonRelease-1>',klik)
master.mainloop()
