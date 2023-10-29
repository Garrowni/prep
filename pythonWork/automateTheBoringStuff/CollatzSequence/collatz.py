#################################
# create a function collatz()
# input parameter is number
# if number is even 
#       print number // 2
#       return number // 2
# if number is odd
#       print 3 * number + 1
#       return 3 * number + 1
##################################
currentNum = int(input("Enter a number: "))
def collatz(number):
    if (number % 2 == 0 ):
        return number // 2
    else:
        return 3 * number + 1


while(currentNum != 1):
    currentNum = collatz(currentNum)
    print(currentNum)










