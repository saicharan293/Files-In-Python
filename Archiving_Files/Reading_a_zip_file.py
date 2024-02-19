import zipfile

#To read files present in a zip file

def read_zip(zipf):
    with zipfile.ZipFile(zipf,'r') as archive:
        lst = archive.namelist()
        for f in lst:
            zipinfo=archive.getinfo(f)
            print(f'{f} => {zipinfo.file_size} bytes, {zipinfo.compress_size} compressed')

read_zip('./files/02/firstZipFile.zip')