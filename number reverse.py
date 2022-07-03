n=int(input("enter number: "))
print("Before reversing the number was: ",n)
reverse=0
while n!=0:
    reverse=reverse*10+n%10
    n=(n//10)
print("after reversing the number is: %d", %reverse)
