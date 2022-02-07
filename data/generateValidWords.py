from itertools import product
import enchant
import json

def numberToWord(numList):
    a = ord('a')
    res = ""
    for num in numList:
        char = chr(num + a - 1)
        res += char
    return res

alphabet = [i for i in range(1, 27)]
SIZE = 5
wordDict = enchant.Dict('en_US')

possible = list(product(alphabet, repeat=SIZE))

print('There are {} possible'.format(len(possible)))

acutalWord = []
count = 0

for i, numList in enumerate(possible):
    word = numberToWord(numList)
    if i % 100000 == 0: 
        print(count)
        count += 1
    if wordDict.check(word):
        acutalWord.append(numList)
        
with open('actualWords.json', 'w') as f:
    json.dump(acutalWord, f)

print('Generate JSON Successful! There are {} valid words'.format(len(acutalWord)))


