##########################################################
# Check if a certain file exists.
##########################################################
import os

path = os.path.expanduser('~/Documents/')

print("------Enter the directory path to recursively search in. The default is ~/Documents. press enter to leave the default")

enteredPath = str(input("Enter directory path: "))
if (len(enteredPath) != 0):
    path = enteredPath

fileName = str(input("Enter file name: "))
if (len(fileName) != 0):
    print("Searching " + path + " for file: " + fileName)
    for root, dirnames, filenames in os.walk(path):
        files = [f for f in filenames]
        if not fileName in files:
            print("Would you like me to create the file? Enter yes, y, or Y and I will make it!")
            if(str(input("Enter your response: "))==("y")or("Y")or("yes")):
                print("Creating folder: " + fileName)
                with open(os.path.join(path,fileName), 'w') as f:
                    f.write("Template Text...")
            else:
                print("The file does not exist and was not created.")
        else:
            print("Complete....")
            print(path + fileName + " exists.")
else:
    print("Did you put anything?")