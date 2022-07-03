from unittest import result


num=int(input("enter the number: "))
exp=int(input("enter the exponent"))
result=1
print(num,"to the power",exp,"=",end='')
for exp in range(exp,0,-1):
    result*=num
print(result)