import zipfile

to_zip=[
    './files/02/demos/files/subfolder/01_file_test.csv',
    './files/02/demos/files/subfolder/01_file_test.txt',
    './files/02/demos/files/subfolder/01_file_test.csv',    
    './files/02/demos/files/subfolder/01_file_test.txt',
    './files/02/demos/files/01_file_test.csv',
    './files/02/demos/files/01_file_test.txt'
    ]

def create_zip(firstZip,files,opt):
    with zipfile.ZipFile(firstZip,opt,allowZip64=True) as archive:
        for f in files:
            archive.write(f)

create_zip('./files/02/firstZipFile.zip',to_zip,'w')