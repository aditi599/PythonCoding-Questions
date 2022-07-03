size=int(input("kitne inputs dene hai??: "))
arr=[ ]
for i in range(0,size):
    elem=int(input("enter the elements: "))
    arr.append(elem)
avg=sum(arr)/size
print("Ang is: ",avg)