import threading

def small(s):
    count=0
    for c in s:

        if c.islower():
            count+=1
    print("number of small elemnts in a string",count)

def capt(s):
    count=0
    for c in s:

        if c.isupper():
            count+=1
    print("number of Captial elemnts in a string",count)
     
def digit(s):
    count=0
    for c in s:

        if c.isdigit():
            count+=1
    print("number of digit elemnts in a string",count)

s=input("Enter a string")
t1=threading.Thread(target=small,args=(s,))
t2=threading.Thread(target=capt,args=(s,))
t3=threading.Thread(target=digit,args=(s,))

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
     