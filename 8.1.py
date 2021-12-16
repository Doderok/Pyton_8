import argparse
import os.path

parser = argparse.ArgumentParser(description='10 строк файла')
parser.add_argument('-file', dest="file")

filename = parser.parse_args().file
isfile = os.path.exists(filename)

if isfile:
    filetxt = (open(filename, 'r'))
    filetxt = filetxt.read()
else:
    filetxt = "Файла не существует"


print(filetxt)