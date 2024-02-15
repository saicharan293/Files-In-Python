import os,fnmatch

def match(folder,search):
    for fi in os.listdir(folder):
        if fnmatch.fnmatch(fi,search):
            print(fi)

# match('./02/demos/files','*_file*.*')
# match('./02/demos/files','*_test*.*')
# match('./02/demos/files','*_file_*.*')
match('./02/demos/files','*2_*_*.*')