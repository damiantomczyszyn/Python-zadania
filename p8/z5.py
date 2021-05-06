
def get_temp(t):
    kelw=t
    return kelw
    


def dekoratorc(old):
    def func(kelw):
        return (-273.15)+old(kelw)
    
    return func

def dekoratorf(old):
    def func(kelw):
        return (old(kelw) - 273.15)* 1.8000 + 32
    
    return func

def fabryka(miara):
    if miara=='celcjusz':
        f=dekoratorc(get_temp)
    else:
        if miara=='fahrenheit':
            f=dekoratorf(get_temp)
            
        else:
            raise TypeError
    return f
    
    
x=int(input('podaj temp w kelw'))
print(get_temp(x))
y=int(input(' temp w celc podaj 1, temp w fahren podaj 2'))
if y == 1:
    get_temp=fabryka('celcjusz')
    print('w celc',get_temp(x))
else:
    get_temp=fabryka('fahrenheit')
    print('w fahren',get_temp(x))


