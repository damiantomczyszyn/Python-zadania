import tkinter as tk
class MyApp(tk.Tk):
    def __init__(self, **packparams):
        super().__init__()
        self.geometry("400x200")
        self.l1=tk.Label(self, text='0 0')
        self.l1.pack(side=tk.TOP, fill=tk.X)
        self.f1=tk.Frame(self, bg='blue')
        self.f1.pack(packparams)
        self.f1.bind('<Button-1>',self.klik)   
    def klik(self, zdarz=None):
        if zdarz:
            self.l1.config(text=str(zdarz.x) + ' ' + str(zdarz.y))
    def myloop(self):
        self.mainloop()
app=MyApp(expand=True, fill=tk.BOTH)
app.myloop()
