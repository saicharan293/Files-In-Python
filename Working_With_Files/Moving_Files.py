import shutil

def mv_files(src,dst):
    shutil.move(src,dst)

# mv_files('./files/02/demos/files/text.txt','./files/02/demos/files/subfolder/text.txt')
# mv_files('./files/02/demos/files','./files/02/demos/xyz')
mv_files('./files/02/demos/xyz','./files/02/demos/files')