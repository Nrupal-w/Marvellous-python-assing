a=int(input("enter a number"))
j=0
for i in range (1,a+1):
  if a%i==0:
    j+=1
  else:
    j=j

if j==2:
  print("Number is  prime")
else:
  print("number is not prime")

