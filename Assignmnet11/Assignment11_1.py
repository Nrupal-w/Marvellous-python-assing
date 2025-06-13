def num(n,current=1):
    if current>n:
        return 
    
    print(current,end="")
    num(n,current+1)
    
a=int(input("Enter a number"))
num(a)
