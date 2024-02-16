import os


#to get all the files present in the given folder and its sub folder if any

def treverse(folder):
    for fldpath,dirs,fls in os.walk(folder):
        print(f'Folder:{fldpath}')
        for fil in fls:
            print(f'\t{fil}')

treverse('./files/02/demos/files')