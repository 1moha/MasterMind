# Name:        Mohammed Mohammud
# Class:       CSC 110 - Spring 2021
# Assignment:  Programming Project Implementation 
# Due Date:    May 3, 2021

# Program title:  Mastermind

# --------------------
# Project Description:
# --------------------
# This project is to make a program that will play the game of Mastermind. with two players 
# one player being the computer(codemaker) and the other player is the human(codebreaker).
# The codemaker will choose the hidden colors, and the codebreaker will attempt to guess the 
# hidden colors. The codemaker will choose 4 colors, and the codebreaker will try to guess those
# four colors. The codebreaker will have 10 guesses maxemum to break the code. The computer(codemaker)
# will than give a clue to the codebreaker each time. There are two clues the codebreaker might receive:
# 2 - if the guess has a correct color in the correct position.
# 1 - if the guess has a correct color, but in the wrong position.

# --------------------
# program
# --------------------
import random
#global
allColors=['red','orange','yellow','green','blue','purple']

# --------------------
# The menu
# --------------------
def menu():
    print("Make a guess of four colors: ")
    for i in range(len(allColors)):
        print(i,' - ',allColors[i])
    print("-------------------------------")

# --------------------
# Code maker function
# --------------------
def makeRandomeColors():
    # This function will make 4 colors randomly using the global list
    codemakerColorsList = []
    # It will return a list containing the four colors
    for i in range(len(allColors) - 2):
        codemakerColorsList.append(allColors[random.randint(0,5)])
    return codemakerColorsList

# ----------------------
# Code breraker function
# ----------------------
def codebreakerGuess(codemakerColorsList):
    # This function will ask the codebreaker to guess the hidden four colors
    # make a list for code breaker's gusses
    codebreakerGuessList = []
    allColorsLength = len(allColors)
    userGuess = 0
    i = 0
    # while the user's guess is greater than the length of all colors  or the counter is less than 5
    while userGuess >= allColorsLength or i < allColorsLength - 2:
        
        # exception handling
        try:
            userGuess = int(input("Guess color: "))
            # if the user's guess is greater than 5
            if userGuess >= allColorsLength:
                # print the following
                print("Please choose a number from 0 to ", allColorsLength - 1)
                # otherwise
            else:
                # Store all the codebreaker's guesses and return a list containg it
                codebreakerGuessList.append(allColors[userGuess])
                i = i + 1
        # if ther is a value error print the following
        except ValueError:
            print("Invalid entry, try again...")
    # return the code breaker's list
    return codebreakerGuessList

# --------------------
# Clues/hints function
# --------------------
def CodebreakerClues(codemakerColorsList, codebreakerGuessList):
    # This function will give guesses to the codebreaker.
    clue = []
    checkedColors = []
    # If the codebreaker guessed the four colors  and its positions within the maximum number allowed
    for i in range(len(codemakerColorsList)):
        # and the color is not checked yet
        if codebreakerGuessList[i] not in checkedColors or codebreakerGuessList[i] == codemakerColorsList[i]:
            if codemakerColorsList[i] == codebreakerGuessList[i]:
                # put 2 in the clue to print for the code breaker
                clue.append(2)
                # append the color to the checked colors list
                checkedColors.append(codebreakerGuessList[i])
            # Otherwise, if the position was incorrect it will display 1 to the codebreaker
            elif codebreakerGuessList[i] in codemakerColorsList:
                # put 1 in the clue to print for the code breaker
                clue.append(1)
                # append the color to the checked color list
                checkedColors.append(codebreakerGuessList[i])
    # Return the clue
    return clue

# ------------------
# the main function
# ------------------
def main():
    codemakerColorsList = makeRandomeColors()
    cBreakerWon = False
    Gusses = 0
    # the code breaker have 10 attempts
    while Gusses < 10:
        # display the menu
        menu()
        codebreakerGuessList = codebreakerGuess(codemakerColorsList)
        clue = CodebreakerClues(codemakerColorsList, codebreakerGuessList)
        print("-------------------------------")
        print("Your guess is: ", codebreakerGuessList)
        print(f"The clue is:    {clue}\n")
        # when the code breaker guesses all colors (the four of them), print the following and exit the code
        if clue.count(2) == 4:
            print("\nCONGRATRS, you broke the code...")
            print("secret code is: ", codemakerColorsList)
            cBreakerWon = True
            break
        Gusses += 1
    # if the code breaker has used all 10 attempts and couldn't guess the colors
    if cBreakerWon == False:
        # print the following
        print("\nyou didn't break the code on time, You lost :(")
        print(f"The secret code is: {codemakerColorsList}\n")

main()
