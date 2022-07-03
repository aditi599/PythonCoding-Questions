i,temp=0,0
n=int(input("enter the number: "))
for i in range(2,n//2):
    if n%i==0:
        temp=1
        break
if temp==1:
    print("not prime")
else:
    print("prime")