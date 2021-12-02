import time
a=float(input("Введите длину первого катета: "))
b=float(input("Введите длину второго катета: "))
s=(a*b)/2
p=(a*a+b*b)**0.5
print("Периметр равен " + str(p)+ " см")
print("Площадь равна " + str(s)+ " см^2")
time.sleep(1000000)
