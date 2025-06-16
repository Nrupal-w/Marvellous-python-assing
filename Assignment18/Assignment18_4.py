import os

def compare(f1,f2):
    fobj1=open(f1,"r")
    fobj2=open(f2,"r")
    data1=fobj1.read()
    data2=fobj2.read()

    if data1==data2:
        print("Contents of both the files are same ")
    else:
        print("Contents of the file are diffrent")

def main():
    print("Enter the name of frist file")
    a=input()
    print("Enter the name of second file")
    b=input()
    compare(a,b)

if __name__=="__main__":
    main()

