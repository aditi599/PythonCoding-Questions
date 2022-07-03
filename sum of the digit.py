def getsum(n):
    sum=0
    for digit in str(n):
        sum+=int(digit)
    return sum
n=int(input("input idhr likho: "))
print(getsum(n))