import shutil

#To copy files or folders from one location to another location
#here location can represent Either "file" or "folder"
def copy_file(src,dest):
    shutil.copy(src,dest)

def copy_folder(src,dest):
    shutil.copytree(src,dest)

source='./files/02/demos/files/02_file.txt'
destination='./files/02/demos/files/subfolder'
source_folder='./files/02/demos/files/subfolder'
destination_folder='./files/02/demos/files/newfolder'
# copy_file(source,destination)
copy_folder(source_folder,destination_folder)