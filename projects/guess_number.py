import random
b=int(input('give the range of your random number:'))
print('now guess the random number!')
def guessing_number(b):
    random_number= random.randint(1,b)
    guess=0
    while guess!=random_number:
        guess=int(input('guess the random number:'))
        if guess>random_number:
            print('your guess is too high')
        elif guess<random_number:
            print('your guess is too low')
    
    print(f'congratulation! you guessed it right.{random_number} is the right random number')    

guessing_number(b)