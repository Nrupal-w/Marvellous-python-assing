a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a > b:
    if a > c:
        print("Largest number is:", a)
    else:
        print("Largest number is:", c)
else:
    if b > c:
        print("Largest number is:", b)
    else:
        print("Largest number is:", c)

        
# This program takes three numbers as input and uses nested if-else statements to find the largest.
# It compares the numbers and prints the largest one among them.
