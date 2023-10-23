import random, sys


print('ROCK, Paper, Scissors')

wins = 0
losses = 0
ties = 0


while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 's' or playerMove == 'p':
            break
        print('Type one for r, p, s, or q.')

    if playerMove == 'r':
        print('Rock versus...')
    elif playerMove == 'p':
        print('Paper versus...')
    elif playerMove == 's':
        print('Scissors vs...')

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    if playerMove == computerMove:
        print('Tie!')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('Win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('Win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('Lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('Lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('Lose!')
        losses = losses + 1

