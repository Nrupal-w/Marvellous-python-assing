a=int(input("Enter a number"))
i=0
while a!=0:
    i=i+(a%10)
    a=a//10
    

print(i)

#used the while loop to chek if a is 0 then moded a with 10 to get the last number and add to i and repating same until getting full answer
