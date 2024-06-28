# This is a guess the number game.
import random

# Generate a random number between 1 and 20
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20.')

# Ask the player to guess the random number.
# Provide them with a maximum number of guesses (6).
for guessesTaken in range(1, 7):
  guess = int(input())

  if guess < secretNumber:
      print('Your guess is too low.')
  elif guess > secretNumber:
      print('Your guess is too high.')
  else:
      break # This condition is the correct guess!

if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
