##########################################################
# Coin Flip Streaks
# write a program that finds out how often a streak of 
# 6 heads or 6 tails comes up in a randomly generated list
# of coin flips.
#
# 2 parts:
# 1 part should generate a list of heads and tails
# 2 part should check if theres a streak
# loop it 10000 times 
# random.randint(0, 1) --> 50% of the times 0, other 50% 1
# Example:
# No Input
# this should return  
##########################################################

import random
numberOfStreaks = 0
#for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
results=[]
for i in range (100):
    results.append(random.randint(0,1))

 
   # Code that checks if there is a streak of 6 heads or tails in a row.
numInRow = 0
currentStreak = [ ]
for i in range(len(results)):
    print("index: " + str(i) + "  value: " + str(results[i]))
    ############
    #to do: determine if 6 in a row are the same
    # add to a counter how many times 6 in a row are the same
print('Chance of streak: %s%%' % (numberOfStreaks / 100))