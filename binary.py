num=int(input("enter the number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("the number is not in binary form")
        break
    num=num//10
    if num==0:
        print("num is binary")