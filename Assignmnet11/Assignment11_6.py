def nat(n):
    if n==0:
        return 0
    return n+nat(n-1)

a=int(input("Enter a number"))
sum=nat(a)
print("sum_n(",a,")",sum) 