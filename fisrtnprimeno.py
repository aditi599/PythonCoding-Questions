
num=int(input("enter range: "))
print("the prime numbers are: ")
for n in range(1,num+1):
    for i in range(2,n):
        if (n%i==0):
            break
    else:
        print(n,end=' ')