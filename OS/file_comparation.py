import os
import sys

#path_source='/home/pi/Desktop/filecomp1/'
#path_target='/home/pi/Desktop/filecomp2/'

#Function takes parameters 1- file path of source system 2-file path of target system
def main (path_source,path_target):
    la_source=[]
    la_target=[]
    diff_out_source=[]
    diff_out_target=[]
    list_source=os.walk(path_source)
    list_target=os.walk(path_target)
    #Make a list for given parameters
    path_iterate=[list_source,list_target]
    counter=0

#Iterate through function parameters    
    for i in path_iterate:
        #Iterate through OS files
        if counter==0:
            print('****Source files with full path****')
        else:
            print('****Target files with full path****')
        for dirpath,dirnames,filenames in i:
            #Iterate through files to join them with file attributes
            for filename in filenames:
                file_with_path=os.path.join(dirpath,filename)
                file_size=os.path.getsize(file_with_path)
                #counter==0 represents source files
                if counter == 0:
                    print(file_with_path,file_size)
                    la_source.append(filename)
                else:
                    print(file_with_path,file_size)
                    la_target.append(filename)
        counter+=1
    #print(la_source)
    #print(la_target)
    print('Files that are not exist in path Target')
    print(list(set(la_source)-set(la_target)))
    print('Files that are not exist in path Source')
    print(list(set(la_target)-set(la_source)))
                        

if __name__== '__main__':
    # Map command line arguments to function arguments.
    main(*sys.argv[1:])



