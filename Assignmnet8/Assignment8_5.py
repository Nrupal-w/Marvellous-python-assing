import threading

def normal():
    for i in range(1,50,1):
        print(i,end=" ")
    
def rever():
    for i in range(50,1,-1):
        print(i,end=" ")
    
t1=threading.Thread(target=normal)
t2=threading.Thread(target=rever)
t1.start()
t1.join()
t2.start()
t2.join()