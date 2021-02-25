lista1=[1,2,3,4,5]
lista2=['a','b','c','d','e']

def funkcja(lista1,lista2):
    lista3=[]
    for i in 0,1,2,3,4:
        
        lista3.append(lista1[i])
        lista3.append(lista2[i])
    return lista3
nowalista=funkcja(lista1,lista2)
print(nowalista)
