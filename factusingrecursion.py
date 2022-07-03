def fac(n):
    if n==1:
        return n
    else:
        return n*fac(n-1)
num=int(input("enter number: "))
print("factorial of the number is: ",fac(num))