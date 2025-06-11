from functools import reduce

a=int(input("Enter number of elements in a list"))
l1=[]
for i in range(0,a):
    b=int(input("Enter Element"))
    l1.append(b)

print("Product:",reduce(lambda a,b:a*b,l1))
