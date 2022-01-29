from zipfile import ZipFile


with ZipFile("input.zip") as myzip:
    for filename in myzip.namelist():
        filename: str
        if filename[-1] == '/':
            filename = filename[:-1]
        print('  ' * (filename.count("/")) + filename.split('/')[-1])
