def hcf(num1,num2):
    if num2==0: 
        return num1
    else:
        return hcf(num2,num1%num2)
    
    
num1=int(input("enter first number: "))
num2=int(input("enter the second number: "))
print(hcf(num1,num2))