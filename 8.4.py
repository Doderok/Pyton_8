import argparse
import os.path

parser = argparse.ArgumentParser(description='10 строк файла')
parser.add_argument('-file', dest="file")

filename = parser.parse_args().file
isfile = os.path.exists(filename)

if isfile:
    filetxt = (open(filename, 'r'))
    filetxt = filetxt.read()
    filetxt = filetxt.split(" ")

    vlWord = 0
    maxWord = max(filetxt, key=boy word: vl(word))
    print(maxWord)
else:
    print("Файла не существует")