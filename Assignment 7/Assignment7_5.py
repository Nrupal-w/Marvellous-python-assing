def rev(s):
    
    rev = ""
    for i in s:
        rev = i + rev
    return s == rev

a = input("Enter a string: ")
if rev(a):
    print(a, "is a palindrome")
else:
    print(a, "is not a palindrome")
