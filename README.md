# Wordle-Cracker
This is a project that will automatic generate possible answer of Wordle.


# How to use
*Just run main.py*

It will call a WodleSolver class which will calculate every possible answer we generate from data's *generateValidWords.py* actualWords.json
The file actualWords.json contains 6602 possible guesses of length of 5 words.
Every time our program will pop out a guess and you can enter wordle's hint by color.

* For example:
```
If the guess pop Not in word list enter 99999
There are 6602 remains
Guess : BAZAR ⬜️🟨⬜️⬜️🟨 There are 95 remains
Guess : DRAWL ⬜️🟩️🟩️⬜️⬜️ There are 14 remains
Guess : PRANA ⬜️🟩️🟩️⬜️⬜️ There are 5 remains
Guess : CRACK ⬜️🟩️🟩️⬜️⬜️ There are 1 remains
Guess : FRAME 11111
```
> ![](https://i.imgur.com/ucM1MRu.jpg)
> ![](https://i.imgur.com/gVAle8G.jpg)


Once you type in 12000
Our program will pop out all invalid guess in WordleSolver.choices by the game's rule

Enjoy your WORDLE!!

> If you interest in algorithm of this project you can check **WordleSolver.py**
