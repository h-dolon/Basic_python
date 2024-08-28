n=1
while n<4:
    n+=1
    guess=int(input('Guess: '))
    if(guess==9):
        print('You win')
        break
else:
    print('You failed')    