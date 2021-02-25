a="abc"
b=12
c=1.5


def func(a):
    t=" jest strg"
    y=" jest float"
    u=" jest int"
    if((isinstance(a, ( str)))):
        print(a, t)
    if((isinstance(a, ( int)))):
        print(a, u)    
    if((isinstance(a, ( float)))):
        print(a, y)
    

func(b)
