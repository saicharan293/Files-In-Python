import zipfile


#To add new files to the existing zip file
to_add=[
    './files/02/demos/files/01_file.csv',
    './files/02/demos/files/01_file.txt'
]

def add_to_zip(firstZip,files,opt):
    with zipfile.ZipFile(firstZip,opt) as archive:
        for f in files:
            lst=archive.namelist()

            if not f in lst:
                archive.write(f)
            else:
                print(f'File already exists in zip: {f}')

#'a' represents append mode for zip file
add_to_zip('./files/02/firstZipFile.zip',to_add,'a')