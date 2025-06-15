import os
import sys
import datetime
import checkparameters

def disply(dirname,ext):

    
    newfile =checkparameters.creat_new_file()
    fobj=open(newfile,"w")


    ans=checkparameters.check_abs_path_exists(dirname)

    fobj.write(f"{ans} \n")
    
    ans=checkparameters.convert_to_abs_path(dirname)
    
    fobj.write(f"{ans} \n")

    ans=checkparameters.check_dir_path_exists(dirname)

    fobj.write(f"{ans} \n")

    ans=checkparameters.check_path_is_directroy(dirname)
    
    fobj.write(f"{ans} \n")
        
    
    for foldername,subfolder,filename in os.walk(dirname):
        for name in filename:
            file_ext = os.path.splitext(name)[1]  
            if file_ext == ext:
                fobj.write(str(name)+"\n")                  
                names=os.path.join(foldername,name)
                fobj.write(str(names)+"\n")

def main():
    boder="-"*54
    print(boder)
    print("--------------- Nrupal  Wakode ----------------")
    print(boder)


    if len(sys.argv)==2:
        
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This application is for finding if the file exists in the directory or not")
            print("This is a directory automation script")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
            print("Use the given script as ")
            print("NameOfDirctory File Extention")
            print("Please provide valid absolute path")
    elif len(sys.argv)==3:
         disply(sys.argv[1],sys.argv[2])

    else :
            print("Invalid number of coomand line arguments")
            print("Use the given flags as : ")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    print(boder)
    print("----------- Thank you for using our script -----------")
    print("---------------- Nrupal Wakode --------------")
    print(boder)
    

if __name__=="__main__":
    main()
