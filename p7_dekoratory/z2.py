class NotInteger(Exception):
    
    def __init__(self):
         print('TO NIE INT')


def dodawanie(x,y):
    
    return x+y
def mnożenie(x,y):
    return x*y

def dekorator(funx):
    def new_fun(x,y):
        print('wywołanie ' + funx.__name__ +' po dekorowaniu: ')
        w=str(funx(x,y))
        calosc = ''
        for n in w:
            if(n=='0'):
                print("zero ",end='')
                calosc+='zero '
            if(n=='1'):
                print("jeden ",end='')
                calosc+='jeden '
            if(n=='2'):
                print("dwa ",end='')
                calosc+='dwa '
            if(n=='3'):
                print("trzy ",end='')
                calosc+='trzy '
            if(n=='4'):
                print("cztery ",end='')
                calosc+='cztery '
            if(n=='5'):
                print("pięć ",end='')
                calosc+='pięć '
            if(n=='6'):
                print("sześć ",end='')
                calosc+='sześć '
            if(n=='7'):
                print("siedem ",end='')
                calosc+='siedem '
            if(n=='8'):
                print("osiem ",end='')
                calosc+='osiem '
            if(n=='9'):
                print("dziewięć ",end='')
                calosc+='dziewięć '
                
        calosc=3
        print(type(calosc))
        if type(calosc) !=str:
            
            raise NotInteger()
        return calosc

               
    return new_fun

print('wywołanie dodawanie ',dodawanie(4,5))
dodawanie=dekorator(dodawanie)
dodawanie(4,5)
print('\n')


print('wywołanie mnożenie ',mnożenie(4,5))
mnożenie=dekorator(mnożenie)
mnożenie(4,5)


