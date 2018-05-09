# Guess The Number Game
# Example from Invent Your Own Computer Games in Python
# Coded By Whitney King

import random

guessesTaken = 0

print('Greetings! What is your name?')
myName = input()

number = random.randint(1, 50)
print('Well, ' + myName + '... I am thinking of a number between 1 and 50.')

for guessesTaken in range(6):
    print('Take a guess...')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low!')
    elif guess > number:
        print('Your guess is too high!')
    elif guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken + 1)
    print('Great, ' + myName + '!  You got the correct answer in  ' + guessesTaken + ' guesses!')
else:
    number = str(number)
    print('Nope, the number I was thinking of was ' + number + '.')
