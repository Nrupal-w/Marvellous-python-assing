from functools import reduce

n=int(input("enter number of elemnts in a list"))
l1=[]
for i in range(0,n):
  a=int(input("Enter a element"))
  l1.append(a)

l2=list(filter(lambda a: a > 1 and all(a%i !=0 for i in range(2,int(a**0.5)+1)),l1))
l3=list(map(lambda a:a*2,l2))
l4=reduce(lambda a,b: a if a>b else b,l3)

print(l2)
print(l3)
print(l4)


#used this formula to find prime number for i in range(2, int(x**0.5)+1))
#used if else statment in reduce function to find the min number 
