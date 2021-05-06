import tkinter as tk
from tkinter import *

#okno główne
root = tk.Tk()
licznik=0
krok=1
#kontrolka 'Button'
def LabelConfig(label,txt):
    label.config(text=txt, fg = "light green", bg = "dark green")


def zwieksz(master,l):
    global licznik
    licznik +=krok
    LabelConfig(l,str(licznik))
    

def zmniejsz(master,l):
    global licznik
    licznik -=krok
    LabelConfig(l,str(licznik))

def przypisz(master,e1):
    global krok
    print(e1.get())
    krok=int(e1.get())

def nowykrok():
    global krok
    print(v.get())
    krok=int(v.get())
 
v=tk.IntVar()
tk.Radiobutton(root, text="op1", variable=v, command=nowykrok, value=1).pack()
tk.Radiobutton(root, text="op2", variable=v, command=nowykrok, value=3).pack()
tk.Radiobutton(root, text="op3", variable=v, command=nowykrok, value=10).pack()
b = tk.Button(root, text ="+", command=lambda :zwieksz(root,l))
a = tk.Button(root, text ="-", command=lambda :zmniejsz(root,l))
c = tk.Button(root, text ="save", command=lambda :przypisz(root,e1))

#umieszczenie kontrolki w oknie głównym metodą pack()
b.pack()
a.pack()
c.pack()
l = tk.Label(root, text =str(licznik))
l.pack()
kr = tk.Label(root, text ='krok = '+str(krok))
kr.pack()
e1=Entry(root)
e1.pack()
#pętla komunikatów
root.mainloop()
