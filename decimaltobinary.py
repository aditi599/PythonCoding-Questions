def dtb(num):
    if num>1:
        dtb(num//2)
    print(num%2,end=' ')
if __name__== '__main__':
    num=24
    dtb(num)
#one line code
print(bin(24)[2: ])