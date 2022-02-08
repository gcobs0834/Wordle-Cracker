# Wordle-Cracker
This repository contains algorithm and solver for the game **[WORDLE](https://www.powerlanguage.co.uk/wordle/)**

# How to use
* Run the program:
```
python main.py
```

It will call a WodleSolver class which will calculate every possible answer we generate from data's *generateValidWords.py* actualWords.json
The file actualWords.json contains 6602 possible guesses of length of 5 words.
Every time our program will pop out a guess and you can enter wordle's hint by color.

* For example:
```
====================
Game: 1
====================
If the guess pop Not in word list enter 99999
There are 6602 remains
Guess : DONNA ⬜️⬜️⬜️⬜️🟨 There are 1298 remains
Guess : CLAMS ⬜️⬜️🟩️🟩️⬜️ There are 4 remains
Guess : TRAMP ⬜️🟩️🟩️🟩️⬜️ There are 1 remains
Guess : FRAME ⬜️🟩️🟩️🟩️⬜️ There are 1 remains
Congratulations!

====================
Game: 2
====================
If the guess pop Not in word list enter 99999
There are 6602 remains
Guess : HAIKU 🟨🟨⬜️⬜️⬜️ There are 125 remains
Guess : GHATS ⬜️🟩️🟩️⬜️🟨 There are 15 remains
Guess : SHALL 🟩️🟩️🟩️⬜️⬜️ There are 9 remains
Guess : SHAPE 🟩️🟩️🟩️⬜️⬜️ There are 3 remains
Guess : SHAWM 🟩️🟩️🟩️⬜️⬜️ There are 2 remains
Guess : SHARD 11102
```
> ![](https://i.imgur.com/oGuokkD.png)
> ![](https://i.imgur.com/AXPpA0Y.png)




Enjoy your WORDLE!!

> If you interest in algorithm of this project you can check **WordleSolver.py**
