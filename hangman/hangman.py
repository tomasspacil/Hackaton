#!/usr/bin/env python3
import random
# define a function for generating a random word
def choose_word():
    f = open('words.txt', 'r')
    words = f.read().splitlines()
    goal = words[round(random.random())*len(words)]
    return goal

word = choose_word()
# print out current state of the game
# for example - We're guessing the word: _ _ _ _ _ _ _ _ _ _
GUESS = list(str(len(word)*'-'))
print("We're guessing the word:", GUESS, word)
life = 0
ok = 0

# main loop
while True:
    # let's get a letter from the user
    letter = input("Guess the letter: ")

    # make sure the letter is only one character
    if len(letter) != 1:
        print('JUST A LETTER! AGAIN!')
        letter = input("Guess the letter: ")
    # print the letter to see if everything is ok by now
    print("You guessed", letter)

    # determine if the letter is in the word
    for x,y in enumerate(word):
        if y == letter:
            GUESS[x] = y
            ok+=1
        else:
            life+=1
    print(GUESS)
    # check if the word is not guessed in its entirety
    if ok == len(GUESS):
        break