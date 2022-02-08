import json
from random import shuffle
from collections import defaultdict

class WordleSolver:
    def __init__(self, choices):
        self.choices = choices
        shuffle(self.choices)
    
    def popOneGuess(self):
        return self.choices.pop()

    def calculateRemain(self, wordleString, guess):
        '''
        wordle = [0, 1, 0, 2, 0] means Black, Green, Black, Yellow, Black
        '''
        Colors = self.buildColorHash(wordleString, guess)
        BLACK, GREEN, YELLOW = 0, 1, 2
        res = []
        for choice in self.choices:
            checkBlack =  self.violateBlack(choice, Colors[BLACK])
            checkGreen =  self.violateGreen(choice, Colors[GREEN])
            checkYellow = self.violateYellow(choice, Colors[YELLOW])
            if checkBlack or checkGreen or checkYellow: # If one violates pop out current choice
                continue
            res.append(choice)
        self.choices = res

    
    def violateBlack(self, choice, blackHash):
        for letter in choice:
            if letter in blackHash:
                return True
        return False
    
    def violateYellow(self, choice, yellowHash):
        for i, letter in enumerate(choice):
            if letter in yellowHash and i in yellowHash[letter]:
                return True
        for letter in yellowHash:
            if letter not in choice:
                return True
        return False
    
    def violateGreen(self, choice, greenHash):
        if greenHash:
            for char, indexSet in greenHash.items():
                for i in indexSet:
                    if choice[i] != char:
                        return True
        return False

    def buildColorHash(self, wordleString, guess):
        wordle = self.getWordleList(wordleString)
        BLACK, GREEN, YELLOW = 0, 1, 2
        Colors = {
            BLACK: defaultdict(set),
            GREEN: defaultdict(set),
            YELLOW: defaultdict(set)
        }

        for i, (color, letter) in enumerate(zip(wordle, guess)):
            Colors[color][letter].add(i)

        deleteLetter = []
        for letter in Colors[BLACK]:
            if letter in Colors[GREEN] or letter in Colors[YELLOW]:
                deleteLetter.append(letter)
        for letter in deleteLetter:
            del Colors[BLACK][letter]

        return Colors
        

    def getNumberOfChoices(self):
        return len(self.choices)

    def numToWord(self, nums):
        res = ""
        for num in nums:
            word = chr(num + ord('a') - 1)
            res += word
        return res.upper()
    
    def getWordleList(self, s):
        res = []
        for letter in s:
            res.append(int(letter))
        return res

def main():
    f = open('./data/actualWords.json')
    choices = json.load(f)
    f.close()
    Solver = WordleSolver(choices)
    print(Solver.getNumberOfChoices())
    guess = Solver.popOneGuess()
    print('Guess {}'.format(Solver.numToWord(guess)))
    wordle = "00120"
    Solver.calculateRemain(wordle, guess)
    print(Solver.getNumberOfChoices())

if __name__ == "__main__":
    main()