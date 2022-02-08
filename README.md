# Wordle-Cracker
This is a project that will automatic generate possible answer of Wordle.


# How to use
*Just run main.py*

It will call a WodleSolver class which will calculate every possible answer we generate from data's *generateValidWords.py* actualWords.json
The file actualWords.json contains 6602 possible guesses of length of 5 words.
Every time our program will pop out a guess and you can enter wordle's hint by color.

* For example:
```
# GUESS
F A S T S
# Wordle
G Y B B B # Green Yellow Black Black Black
1 2 0 0 0 # You type in input
```
> ![](https://i.imgur.com/ucM1MRu.jpg)
> ![](https://i.imgur.com/gVAle8G.jpg)


Once you type in 12000
Our program will pop out all invalid guess in WordleSolver.choices by the game's rule

Enjoy your WORDLE!!

> If you interest in algorithm of this project you can check **WordleSolver.py**
