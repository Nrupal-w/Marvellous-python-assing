import os
import sys

def dirwatch(filename):
   
    flag=os.path.exists(filename)
    if flag==False:
        exit()
    
    fobj=open(filename,"r")
    data=fobj.read()
    print("The contents of the file is \n")
    print(data)

def main():
    print("Enter the name of your file")
    a=input()
    dirwatch(a)

if __name__=="__main__":
    main()


