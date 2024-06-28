"""
  Scenario: Write a Python program that generates 
  a random number between either 1 - 10, 1 - 100,
  or 1 - 1000 and asks the user to guess said number.  
     
  See the following URL: https://pythonspot.com/random-numbers/

  # Generates a random integer between 1 and either 10, 100, or 1000.

                  Requirements:
                  =============
  a)	Create constants for minimum guess (1), maximum guess (10, 100,
      or 1000) and any string error text desired.

  b)	At the end of each guessing game iteration, ask 
      the user if s/he wants to run the program again and 
      let them do so indefinitely if/as desired.

  c)	Put in code to clear all variables at the beginning 
      of each program run.

  d)	Put in the code that generates a random number from 
      1 to 10, 100, or 1000 (use the constants).

  e)	Put in the code that lets the user make a guess. 

  f)	Put in the code to determine the guess status 
      (invalid, too low, too high, or correct guess).

    If a guess is non-numeric, < 1 or > 10, 100,
    or 1000, the program should display "All guesses must 
    be numbers between 1 - 10, 100, or 1000.  Please try again."
    Do not increment total guesses.

    If a guess (e.g., 67) is higher/lower than the 
    generated random number, the program should display 
    "The guess of 67 is too low/high. Please try again."  
    Do increment total guesses.

    If a guess (e.g., 67) is correct, the user should be 
    given an associated message like "The guess of 67 in 4 
    guesses was correct!"  Do increment total guesses.

  g)	The program should continue to solicit user guesses 
      until the user correctly guesses the random number 
      and then print out the message as shown above. Let 
      the user continue to "play the game" as many times 
      as desired, generating a new random number each time.

  The GuessingGame03JPS.py program demonstrates:
  1.  import from
  2.  as
  3.  if
  4.  def
  5.  return
  6.  print
  7.  str
  8.  try
  9.  except
  10. finally
  11. raise
  12. global
  13. multiline Python comments (""" """)
"""

from random import randint
import math
import os
import sys

#  Declare and initialize numeric constants
MINNUMBER     =    1
MAXNUMBEREZ   =   10
MAXNUMBERMED  =  100
MAXNUMBERHARD = 1000

#  Declare and initialize string constants
ILLGUESS = "Illegal Guess. Must Be A Number Between 1 - 100"
TGO      = "The Guess Of "
TOOHIGH  = " Was Too High. "
TOOLOW   = " Was Too Low. "
CORRECT  = " Was Correct In "
PTA      = "Please Try Again."

#  Declare and initialize global variables
numberToGuess = 0           # Number to guess 
guess         = 0           # Current guess
totalGuesses  = 0           # Total guesses this game
maxNum        = 0           # Maximum number allowed this game
runAgain      = True        # Let user play another game if desired

# Determine which game to play, i.e.
def determineGameToPlay():
  global numberToGuess
  global maxNum
  os.system('clear')
  #print("About to call setUpperLimit()")
  maxNum = setUpperLimit( 'Enter maximum number to guess:' +
                          '\n1 for a random number between 1 and 10'  +
                          '\n2 for a random number between 1 and 100' +
                          '\n3 for a random number between 1 and 1000' +
                          '\nPlease enter a 1, 2, or 3 now:\t')
  if(maxNum == 0):
    os.system('clear')
    determineGameToPlay()
  
  playTheGame(maxNum)

def setUpperLimit(prompt):
  global numberToGuess
  #print(prompt)
  upperLimit = 0
  userInput = input(prompt)
  try:
    match userInput:
      case '1':
        upperLimit = MAXNUMBEREZ
      case '2':
        upperLimit = MAXNUMBERMED
      case '3':
        upperLimit = MAXNUMBERHARD
      case _ :
        raise ValueError
  except ValueError:
      # If conversion fails, inform user, prompt again
      print("Invalid input. Please enter a 1, 2, or 3 only.")
      setUpperLimit(prompt)
      os.system('clear')
      return 0
    
  if(upperLimit > 0):
    numberToGuess = randint(1, upperLimit)  # Generate random number
    #print("Random number generated was: " + str(numberToGuess))
    
    #print('Returning now. upperLimit = ' + str(upperLimit))
    return upperLimit

def playTheGame(maxNum):
  global totalGuesses
  global numberToGuess
  # Make guess
  guess = ""
  guess = input('Enter a number between ' +
                str(MINNUMBER) + ' and '  + 
                str(maxNum) + ':\t')

  # Validate guess for no input or non-numeric input
  if (str(guess) == "" or 
      math.isnan(int(guess)) or
      int(guess) < MINNUMBER or
      int(guess) > maxNum):
    print('INVALID GUESS\n ' +
          'Enter a number between ' +
          str(MINNUMBER) + ' and ' + str(maxNum) + ':\t')
    playTheGame(maxNum)

  # Guess was valid. Increment total # guesses
  totalGuesses += 1
  #print("Valid guess counter incremented")

  if (int(guess) < numberToGuess):
    print(TGO + guess + TOOLOW + PTA)
    playTheGame(maxNum)
  elif (int(guess) > numberToGuess):
    print(TGO + guess + TOOHIGH + PTA )
    playTheGame(maxNum)
  else:
    print(TGO + guess + CORRECT + str(totalGuesses ) + " Guesses")
    numberToGuess = 0
    totalGuesses = 0
    playGameAgain()

def playGameAgain():
  global runAgain
  again = input('Run the program again? (Y/N)\t')
  yesNo = again.upper()
  firstChar = yesNo[0]
  if (firstChar != "Y"):
    runAgain = False
    os.system('clear')
    exit()
  else:
    determineGameToPlay()

determineGameToPlay()
