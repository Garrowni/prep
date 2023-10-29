#Task:
#Convert all lower case to upper case and all upper case to lower case
#example PythonROCKS 2 --> pYTHONrocks 2
#no imports allowed

userString = input("Enter the string: ")
print(userString)

alphabet=[chr(i) for i in range(ord('a'),ord('z')+1)]
print(alphabet)
alphabetCap=[chr(i).upper() for i in range(ord('A'),ord('Z')+1)]
print(alphabetCap)

endString=""
for i in userString:
    for index,x in enumerate(alphabet):
        if (i == x):
            print("HIT")
            endString += alphabetCap[index]    
            break         
    for index,y in enumerate(alphabetCap):
        if (i == y):
            print("HIT")
            endString += alphabet[index]
            break
print(endString)

