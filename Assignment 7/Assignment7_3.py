a=int(input("Enter number of elements in a list"))
l1=[]
for i in range(0,a):
    b=int(input("Enter Element"))
    l1.append(b)

print("Even Numbers:",list(filter(lambda a:a%2==0,l1)))
