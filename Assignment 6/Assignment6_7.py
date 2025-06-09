a1=int(input("Enter a number"))
a2=int(input("Enter a number"))
a3=int(input("Enter a number"))
a4=int(input("Enter a number"))
a5=int(input("Enter a number"))
max=0
if(a1>a2 and a1>a3 and a1>a4 and a1>a5):
 max=a1
elif(a2>a1 and a2>a3 and a2>a4 and a2>a5):
 max=a2
elif(a3>a1 and a3>a2 and a3>a4 and a3>a5):
 max=a3
elif(a4>a1 and a4>a3 and a4>a2 and a4>a5):
 max=a4
else:
 max=a5
print("Maximum number is :",max)

# This program takes five numbers as input and determines the maximum among them.
# It uses a series of if-elif-else conditions to compare and find the largest number.
