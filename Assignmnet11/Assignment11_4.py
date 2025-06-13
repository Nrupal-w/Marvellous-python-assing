def pow(n,m):
    if m==0:
        return 1
    return n*pow(n,m-1)

a=int(input("enter a number"))
b=int(input("enter a number"))
sum=pow(a,b)
print("power(",a,",",b,")=",sum)