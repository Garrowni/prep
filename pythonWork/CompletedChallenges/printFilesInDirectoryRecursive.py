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

# get the directory
# make a loop to go through everything in a directory
    # if its a directory call the function on itself
    # if its a file print it out
 