import argparse
import os.path

parser = argparse.ArgumentParser(description='Файл')
parser.add_argument('-file1', dest="file1")
parser.add_argument('-file2', dest="file2")

file1 = parser.parse_args().file1
file2 = parser.parse_args().file2

isfile1 = os.path.exists(file1)
isfile2= os.path.exists(file2)

if isfile1 and isfile2:

    fileData1 = (open(file1, 'r'))
    fileData1 = fileData1.read()
    fileData2 = (open(file2, 'r'))
    fileData2 = fileData2.read()

    print(fileData1 + fileData2)