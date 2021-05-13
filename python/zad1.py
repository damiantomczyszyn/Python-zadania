import tkinter as tk
import tkinter.messagebox
def klik():
    tk.messagebox.showinfo(title='Klik!',message='To był klik!')
master=tk.Tk()# parametr 'command' to adres funkcji -nie można przekazać parametrów # bezpośrednio    
b1=tk.Button(master,text="b1", command=klik)
b1.pack()
master.mainloop()
