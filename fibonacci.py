n=int(input("enter input: "))
def reverse(num):
    if num<10:
        return num
    else:
        return int(str(num%10) + str(reverse(num//10)))
def ispalindrome(num):
    if num == reverse(num):
        return 1
    return 0
if ispalindrome(n)==1:
    print("palindrome")
else:
    print("not palindrome")
