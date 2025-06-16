import os
import sys

def filefiner(data):
    flag=os.path.exists(data)
    if flag==True:
        print("The file exists in the current directory")
    else:
        print("The file dose not exist in the current directory")

def main():
    print("Enter the name of the file you wnat to search for")
    a=input()
    filefiner(a)

if __name__=="__main__":
    main()
    
