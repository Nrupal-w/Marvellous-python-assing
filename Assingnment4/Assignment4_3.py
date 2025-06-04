from functools import reduce


l1=[]

for i in range(0,10):
    a=int(input("Enter a number"))
    l1.append(a)


f=lambda l1: l1>=70 and l1<=90
f2=lambda l1: l1+10



l2=list(filter(f,l1))
l3=list(map(f2,l2))
l4=reduce(lambda a,b:a*b,l3)
print(l2)
print(l3)
print(l4)

#used filter function to filter using the lamda function
#used map function to add 10 to the new created list with the restriction given
#used reduce function to find the product of all elemnet in the new list
