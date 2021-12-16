import argparse
import os.path

parser = argparse.ArgumentParser(description='10 строк файла')
parser.add_argument('-file', dest="file")

filename = parser.parse_args().file
isfile = os.path.exists(filename)

if isfile:
    filetxt = (open(filename, 'r'))
    filetxt = filetxt.read()
    filetxt = filetxt.split("\n")

    num = 0
    arr_num = []
    for i in filetxt:
        if i.startswith("def"):
            arr_num.append(num)
        num += 1

    num2 = 0
    for i in arr_num:
        filetxt.insert(i + num2, "#func")
        num2 += 1

    newFile = open("newDefFile.py", 's')

    for i in filetxt:
        newFile.write(i)
        newFile.write("\n")