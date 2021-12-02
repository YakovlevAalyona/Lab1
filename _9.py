import time
print("Внесите значения: ")
a1=float(input("a1= "))
b1=float(input("b1= "))
c1=float(input("c1= "))
d1=float(input("d1= "))
a2=float(input("a2= "))
b2=float(input("b2= "))
c2=float(input("c2= "))
d2=float(input("d2= "))
a3=float(input("a3= "))
b3=float(input("b3= "))
c3=float(input("c3= "))
d3=float(input("d3= "))


delta= a1 * b2 * b3 + b1 * c2 * a3 + c1 * a2 * b3 - c1 * b2 * a3 - b1 * a2 * c3 - a1 * c2 * b3
delta1 = d1 * b2 * c3 + b1 * c2 * d3 + c1 * d2 * b3 - c1 * b2 * d3 - b1 * d2 * c3 - d1 * c2 * b3
delta2 = a1 * d2 * c3 + d1 * c2 * a3 + c1 * a2 * d3 - c1 * d2 * a3 - d1 * a2 * c3 - a1 * c2 * d3
delta3 = a1 * b2 * d3 + b1 * d2 * a3 + d1 * a2 * b3 - d1 * b2 * a3 - b1 * a2 * d3 - a1 * d2 * b3

if delta !=0:
    x = delta1 / delta
    y = delta2 / delta
    z = delta3 / delta
    print("Результат: " + "x=" + str(x) + "  y=" + str(y) + "  z=" + str(z  ))
else:
    print("Ошибка, детерменант не должен равняться нулю")
time.sleep(10000)