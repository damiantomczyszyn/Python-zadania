
def wpisz_do_listy(n):
   lista = []
   i=n
   while i != 0:
      if i%3 is 0 or i%7 is 0:
         lista.append(i)
      i=i-1
   return lista

lista = wpisz_do_listy(15)
print(lista)
        
