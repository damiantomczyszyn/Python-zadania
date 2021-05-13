import tkinter as tk
def klik(zdarz=None):
    if zdarz:    #pobranie dodatkowej informacji o zdarzeniu
        l1.config(text=str(zdarz.x) + ' ' + str(zdarz.y))
master=tk.Tk()
master.geometry("400x200")
l1=tk.Label(master, text='0 0')
l1.pack(side=tk.TOP, fill=tk.X)
f1=tk.Frame(master, bg='blue')
f1.pack(expand=True, fill=tk.BOTH)
f1.bind('<Button-1>',klik)
master.mainloop()
