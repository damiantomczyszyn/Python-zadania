def fib(n):
   pwyrazy = (0, 1)
   a, b = pwyrazy
   print(a, end=" ")
   while n > 1:
      print (b, end=" ")
      a, b = b, a + b
      n -= 1


n = int(input("Podaj nr wyrazu: "))
fib(20)
print(" \n")
fib(n)

