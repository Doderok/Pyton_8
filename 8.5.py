import argparse
import os.path
import random

parser = argparse.ArgumentParser(description='10 строк файла')
parser.add_argument('-file', dest="file")

filename = parser.parse_args().file
isfile = os.path.exists(filename)

if isfile:
    filetxt = (open(filename, 'r'))
    filetxt = filetxt.read()
    filetxt = filetxt.split("\n")

    arr1 = []
    arr2 = []
    for i in filetxt:
        i = i.split(", ")
        arr1.append(i[0])
        arr2.append(i[1])

    result = str.capitalize(random.choice(arr1)) + str.capitalize(random.choice(arr2))
    print(result)


else:
    print("Файла не существует")