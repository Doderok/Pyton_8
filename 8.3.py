import argparse
import os.path

parser = argparse.ArgumentParser(description='Файл')
parser.add_argument('-file', dest="file")

filename = parser.parse_args().file
isfile = os.path.exists(filename)

if isfile:

    filetxt = (open(filename, 'r'))
    filetxt = filetxt.read()
    filetxt = filetxt.split("\n")

    newFile = open("newFile.txt", 'w')
    for i in filetxt:
        newFile.write("1: " + i)
        newFile.write("\n")
else:
    print("Файла не существует")