def sumnum(n):
    if n==0:
        return 0
    
    return n%10+sumnum(n//10)
    

a=int(input("Enter a number"))
sum=sumnum(a)
print("sum_of_digits(",a,")=",sum)