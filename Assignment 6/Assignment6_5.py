a=int(input("enter a number"))
j=0
for i in range(2,a+1):
    if a%i==0:
        j=j+1

if j==1:
    print(a,"is prime number")
else:
    print(a,"is not a prime number")


# This program checks whether a given number is a prime number.
# It counts the number of factors and prints whether the number is prime or not.
