import os


def count(data,name):
    flag=os.path.exists(data)
    if flag==False:
        exit()
    fobj=open(data,"r")
    temp=fobj.read()
    word=temp.split()
    i=word.count(name)
    
    print(f"Frequency of the word {name} is {i}")

def main():
    print("Enter the name of the file")
    a=input()
    print("Enter the word you wnat to search")
    b=input()
    count(a,b)

if __name__=="__main__":
    main()





