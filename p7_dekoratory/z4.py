
globalna = 0
def dodawanie(x,y):
    
    return x+y
def mnożenie(x,y):
    return x*y

def dekorator(funx):
    #globalna+=1
    def new_fun(x,y):
        global globalna
        print('wywołanie funkcji ' + funx.__name__ +' po dekorowaniu nr: ',globalna)
        funx(x,y)
        globalna+=1
        
            
        return globalna       
    return new_fun

print(globalna)
print('wywołanie dodawanie ',dodawanie(4,5))
dodawanie=dekorator(dodawanie)
dodawanie(4,5)
print('\n')

print(globalna)
print('wywołanie mnożenia ',mnożenie(4,5))
mnożenie=dekorator(mnożenie)
mnożenie(4,5)
lista = [1,2,3,4,5,6,7]
for x in lista:
    mnożenie(4,5)
print(mnożenie(4,5))
