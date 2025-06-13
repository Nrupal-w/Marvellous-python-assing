def coun(n,count=0):
    if n==0:
        return 1
    
    if n<10:
        return 1 if n==0 else 0
    return(1 if n%10==0 else 0)+coun(n//10)

a=int(input("Enter a number"))
ans=coun(a)
print("count_zero(",a,")=",ans)
