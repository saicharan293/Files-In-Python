from pathlib import Path

def glob_match(folder,search):
    p=Path(folder)
    for i in p.glob(search):
        print(i)

# glob_match('./02/demos/files','*2*.t*')
glob_match('./02/demos/files/subfolder','*_file_*.t*')