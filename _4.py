import time
a=int(input("Введите a: "))
b=int(input("Введите b: "))
a=a+b
b=a-b
a=a-b
print("меняем местами")
print("первое число: " + str(a))
print("второе число: " + str(b))
time.sleep(100000)
