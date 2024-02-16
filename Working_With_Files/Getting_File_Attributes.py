import os
from datetime import datetime

# the purpose of the code is to retrieve human readable time at which selected file is created

def get_Date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d %b %y')

def get_file(folder):
    with os.scandir(folder) as dir:
        for files in dir:
            if files.is_file():
                inf=files.stat()
                print(f'Modified date is {get_Date(inf.st_mtime)} {files.name}')

get_file('./files/02/demos/files/subfolder')