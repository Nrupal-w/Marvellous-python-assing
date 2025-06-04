from functools import reduce
l1=[]
n=int(input("Number of elements in list"))
for i in range(0,n):
    a=int(input("Enter a number"))
    l1.append(a)

l2=list(filter (lambda a: a%2==0,l1))
l3=list(map(lambda a:a**2,l2))
l4=reduce(lambda a,b:a+b,l3)

print(l2)
print(l3)
print(l4)

# Filters even numbers, squares them, and sums the result using lambda, filter, map, and reduce.
# Displays the even numbers, their squares, and the final sum.

