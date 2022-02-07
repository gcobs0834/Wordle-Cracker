from WordleSolver import WordleSolver
import json


f = open('actualWords.json')
choices = json.load(f)
f.close()
Solver = WordleSolver(choices)

while True:
    score = ""
    currentRemaining = Solver.getNumberOfChoices()
    print("{} possible remains".format(currentRemaining))
    guess = Solver.popOneGuess()
    guessWord = Solver.numToWord(guess)
    print("Guess {}".format(guessWord))
    wordle = ""
    while len(wordle) != 5 and not wordle.isdigit():
        print('If you find word not in list enter 99999')
        wordle = input('Enter Wordle\'s Color Hint : ')
        
    if wordle == '99999':
        continue
    if wordle == '11111':
        print('Congratulations!')
        break
    Solver.calculateRemain(wordle, guess)
    

