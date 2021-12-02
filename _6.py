n = int(input())
mult=1
while n > 0:
    digit=n%10 
    mult=mult*digit
    n=n//10

print(mult)




