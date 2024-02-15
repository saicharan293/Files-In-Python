import os

def ends_with(folder,word):
    for file_name in os.listdir(folder):
        if file_name.endswith(word):
            print(file_name)

# ends_with('./02/demos/files','.txt')
def starts_with(folder,word):
    for file_name in os.listdir(folder):
        if file_name.startswith(word):
            print(file_name)

starts_with('./02/demos/files','01_test')