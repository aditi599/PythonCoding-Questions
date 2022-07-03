from math import factorial


n=int(input("enter the number: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i
print("the factorial is: ",factorial)