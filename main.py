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

f = open('./data/actualWords.json')
choices = json.load(f)
f.close()
Solver = WordleSolver(choices)

print('If the guess pop Not in word list enter 99999')
guessWord = ""
colors = ""
while True:
    currentRemaining = Solver.getNumberOfChoices()
    printGuess(guessWord, colors, currentRemaining)
    guess = Solver.popOneGuess()
    guessWord = Solver.numToWord(guess)
    wordle = ""
    while len(wordle) != 5 and not wordle.isdigit():
        wordle = input("Guess : {} ".format(guessWord))
    if wordle == '99999':
        continue
    if wordle == '11111':
        print('Congratulations!')
        break
    print ('\033[1A''\033[F')
    colors = stringToColor(wordle)
    Solver.calculateRemain(wordle, guess)
    

