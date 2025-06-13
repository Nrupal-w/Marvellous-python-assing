def pattern(n,count=1):
    if count==n:
     print("*"*n)
     return 0
    print("*"*count)
    pattern(n,count=count+1)

a=int(input("Enter number "))
pattern(a)

    