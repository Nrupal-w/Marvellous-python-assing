from threading import *

class even(Thread):
    def run(self):
        i=1
        j=1
        while i<=10:
            if j%2==0:
                print(j)
                i+=1
            j+=1

class odd(Thread):
    def run(self):
        i=1
        j=1
        while i<=10:
            if j%2!=0:
                print(j)
                i+=1
            j+=1

t1=even()
t2=odd()

t1.start()
t2.start()
t1.join()
t2.join()
