import math as m

a = float(input("A = "))
b = float(input("B = "))

if a > 0 and b > 0:
   c = pow(a, 2) + pow(b, 2)

   print("S = {}".format(round(m.sqrt(c), 2)))
   print("P = {}".format(round(a+b+m.sqrt(c),2)))

else:
   print("Стороны не могут быть < 0")
