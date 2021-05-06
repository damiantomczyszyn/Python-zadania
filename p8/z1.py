import tkinter as tk
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
    

b = tk.Button(root, text ="+", command=lambda :zwieksz(root,l))
a = tk.Button(root, text ="-", command=lambda :zmniejsz(root,l))
#umieszczenie kontrolki w oknie głównym metodą pack()
b.pack()
a.pack()
l = tk.Label(root, text =str(licznik))
l.pack()
kr = tk.Label(root, text ='krok = '+str(krok))
kr.pack()
#pętla komunikatów
root.mainloop()
