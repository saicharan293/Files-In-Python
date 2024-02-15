import os,fnmatch

def match(folder,word):
    for fi in os.listdir(folder):
        if fnmatch.fnmatch(fi,word):
            print(fi)

# match('./02/demos/files','*.csv')
# match('./02/demos/files','*_file.csv')
match('./02/demos/files','*1*_file.csv')