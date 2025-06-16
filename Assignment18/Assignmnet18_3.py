import os
import time

def filecopy(data):

    
    fobj=open(data,"r")
    fobj1=open("Demo.txt","w")
    temp=fobj.read()
    fobj1.write(temp)
    fobj.close()
    fobj1.close()

def main():
    print("Enter the name of the file")
    a=input()
    filecopy(a)

if __name__=="__main__":
    main()

