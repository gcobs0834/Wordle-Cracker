from collections import defaultdict
import json

f = open('actualWords.json')
choices = json.load(f)
f.close()

def wordToNum(word):
    res = []
    for s in word:
        num = ord(s) - ord('a') + 1
        res.append(num)
    return res
print('Generate JSON Successful! There are {} valid words'.format(len(choices)))
toRemove = ['xrefs', 'xxxix', 'xxxiv', 'xxxii', 'xxvii', 'xxiii', 'xviii', 'xcvii']

numLists = [wordToNum(i) for i in toRemove]

for word in numLists:
    choices.remove(word)

with open('actualWords.json', 'w') as f:
    json.dump(choices, f)

print('Generate JSON Successful! There are {} valid words'.format(len(choices)))