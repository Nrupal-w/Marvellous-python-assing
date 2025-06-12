import threading

def even(lst,n):
    sum=0
    for i in range (0,n):
          if lst[i]%2==0:
               sum+=lst[i]
    
    print("Addation of all even numbers in the lis is ",sum)

def odd(lst,n):
    sum=0
    for i in range (0,n):
          if lst[i]%2!=0:
               sum+=lst[i]
    
    print("Addation of all odd numbers in the lis is ",sum)

lst=[]
n=int(input("Enter numer of elemnts in a list"))
for i in range(n):
 a=int(input("Enter the element"))
 lst.append(a)


t1=threading.Thread(target=even,args=(lst,n,))
t2=threading.Thread(target=odd,args=(lst,n,))

t1.start()
t2.start()
t1.join()
t2.join()

    

    
