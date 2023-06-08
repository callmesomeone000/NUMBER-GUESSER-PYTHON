import random

toprange=int(input('Enter the top range for a number: '))
number=random.randint(1, toprange+1)

running=True
while running:
    guess=int(input('Guess the number: '))

    if guess == number:
        print('You guessed it right!!!')
        running=False
    elif guess<number:
        print('Too low')
    else:
        print('Too low')
