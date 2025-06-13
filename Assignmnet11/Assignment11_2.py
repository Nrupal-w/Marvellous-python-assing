def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)
    

a=int(input("Enter a number "))
sum=fac(a)
print("Factorial(",a,")=",sum)
    