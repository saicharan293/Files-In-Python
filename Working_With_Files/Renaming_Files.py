import os
from pathlib import Path

#To rename a file present in any folder
def ren_file(src,dst):
    os.rename(src,dst)

def ren_file_2(src,dst):
    f=Path(src)
    f.rename(dst)
source='./files/02/demos/files/text.txt'
destination='./files/02/demos/files/test.txt'
# ren_file(source,destination)
ren_file_2(destination,source)