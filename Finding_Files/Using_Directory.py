import os

def list_dir(folder):
    for f in os.listdir(folder):
        print(f)

list_dir('./02/demos/files')
