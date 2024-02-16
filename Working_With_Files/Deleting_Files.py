import os

#To delete a file present in folder
def remove_file(f):
    if os.path.isfile(f):
        try:
            os.remove(f)
        except OSError as e:
            print(f'Error: {f} : {e.strerror}')
        
    else:
        print(f'Error : {f} is not a valid file')
source='./files/02/demos/files/text.txt'
remove_file(source)