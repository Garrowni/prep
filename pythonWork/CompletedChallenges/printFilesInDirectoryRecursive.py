import os

def recursivelyPrintFiles(parentDir):
    for childDir in os.listdir(parentDir):
        childDir = os.path.join(parentDir, childDir)
        if os.path.isdir(childDir):
            recursivelyPrintFiles(childDir)
        else:
            print(childDir)

path = str(input("Enter a path to recursively print files from: "))
recursivelyPrintFiles(path)
