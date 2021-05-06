def fun(*args): #funkcja przed dekoracją
    #print(args)
   # print(type(args))
    suma=0
    for x in args:
        suma+=x
    return suma

#fun("a","b","c",1,3,5) #wywołanie funkcji
def dekoruj(old_fun): #dekorator
    def new_fun(*args):
        nargs=[]
        for x in args:
            if type(x) == int:
                nargs.append(x)
       # print('\n\n',type(nargs))
       # print('\n\n',(nargs))
        args=tuple(nargs)
       # print('\n\n',type(nargs))
       # print('\n\n',(nargs))
        return old_fun(*nargs)
    return new_fun

print(fun(1,3,5))

fun=dekoruj(fun) #dekorowanie
print('---po dekoracji---')
print(''' z argumentami "a","b","c",1,3,5''')
print(fun("a","b","c",1,3,5))
