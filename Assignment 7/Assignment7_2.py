a=int(input("Enter number of elements in a list"))
l1=[]
for i in range(0,a):
    b=int(input("Enter Element"))
    l1.append(b)

print("Doubled List ",list(map(lambda a: a*2,l1)))
