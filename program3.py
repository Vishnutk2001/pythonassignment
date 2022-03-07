def isPalindrome(a):
    return a == a[:: -1]
x="malayalam"
result = isPalindrome(x)
if result:
    print("palindrome")
else:
    print("not palindrome")