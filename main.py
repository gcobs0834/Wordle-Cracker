from random import choices
from turtle import color
from WordleSolver import WordleSolver
import json

def stringToColor(s):
    res = ""
    for num in s:
        if num == '0':
            res += '⬜️'
        elif num == '1':
            res += '🟩️'
        else:
            res += '🟨'
    return res

def printGuess(guess, wordle, remain):
    if guess and wordle:
        print("Guess : {} {} There are {} remains".format(guess, wordle, remain))
    else:
        print("There are {} remains".format(remain))

def loadJson(jsonURL):
    f = open(jsonURL)
    choices = json.load(f)
    f.close
    return choices

def main():
    choices = loadJson('./data/actualWords.json')
    Solver = WordleSolver(choices)

    print('If the guess pop Not in word list enter 99999')
    guessWord, colors = "", ""

    while True:
        currentRemaining = Solver.getNumberOfChoices()
        printGuess(guessWord, colors, currentRemaining)

        guess = Solver.popOneGuess() # In number
        guessWord = Solver.numToWord(guess) # In char
        wordle = ""
        while len(wordle) != 5 and not wordle.isdigit():
            wordle = input("Guess : {} ".format(guessWord))
        if wordle == '99999':
            continue
        print ('\033[1A''\033[F') # To clean print
        colors = stringToColor(wordle)
        Solver.calculateRemain(wordle, guess)
        if wordle == '11111':
            printGuess(guessWord, colors, currentRemaining)
            print('Congratulations!')
            break
    

if __name__ == "__main__":
    main()