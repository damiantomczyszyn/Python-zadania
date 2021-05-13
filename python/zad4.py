import tkinter as tk

class MyFrame(tk.Frame):
    def __init__(self, parent, **packparams):
        super().__init__(parent)
        self.pack(packparams)
        self.l1=tk.Label(self, text='0 0')
        self.l1.pack(side=tk.TOP, fill=tk.X)
        self.f1=tk.Frame(self,bg='blue')
        self.f1.bind('<Button-1>',self.klik)
        self.f1.pack(packparams)
    def klik(self, zdarz=None):
        if zdarz:
            self.l1.config(text=str(zdarz.x) + ' ' + str(zdarz.y))

master=tk.Tk()
master.geometry("400x200")
mf=MyFrame(master, expand=True, fill=tk.BOTH)
master.mainloop()
