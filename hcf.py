#hcf
num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
if num1>num2:
    minimum=num2
else:
    minimum=num1
for i in range(1,minimum+1):
    if((num1%i==0) and (num2%i==0)):
        hcf=i
print("the hcf of num1 and num2 is: ",hcf)
