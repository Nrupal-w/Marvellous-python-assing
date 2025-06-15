import os
import sys
import datetime
import checkparameters

def disply(dirname,ext1,ext2):
     
    newfile=checkparameters.creat_new_file()
    fobj=open(newfile,"w")

    ans=checkparameters.check_abs_path_exists(dirname)

    fobj.write(f"{ans} \n")
    
    ans=checkparameters.convert_to_abs_path(dirname)
    
    fobj.write(f"{ans} \n")

    ans=checkparameters.check_dir_path_exists(dirname)

    fobj.write(f"{ans} \n")

    ans=checkparameters.check_path_is_directroy(dirname)
    
    fobj.write(f"{ans} \n")
    
    for foldername,subfoldername,filename in os.walk(dirname):
        for fname in filename:
            file_ext=os.path.splitext(fname)[1]
            if file_ext==ext1 or file_ext==ext2:
                old_path = os.path.join(foldername, fname)
                new_name = os.path.splitext(fname)[0] + ext2
                new_path = os.path.join(foldername, new_name)
                os.replace(old_path,new_path)
                
                fobj.write(f"{fname}\n")
                fobj.write(f"The Path of the file is {new_path}\n")
            
    

def main():
    boder="-"*54
    print(boder)
    print("--------------- Nrupal  Wakode ----------------")
    print(boder)


    if len(sys.argv)==3:
        
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This application is for finding if the file exists in the directory or not")
            print("This is a directory automation script")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--u"):
            print("Use the given script as ")
            print("NameOfDirctory File Extention")
            print("Please provide valid absolute path")
    elif len(sys.argv)==4:
         disply(sys.argv[1],sys.argv[2],sys.argv[3])

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