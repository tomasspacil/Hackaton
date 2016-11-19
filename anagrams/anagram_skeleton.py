#!/usr/bin/env python3

# define a function to load the dictionary to internal structure
# we will load it from external file
def load_dict():
    f = open('words.txt', 'r')
    words = f.read().splitlines()
    return words




# process the input word we're working with
interested = 'tea'
interested_sorted = ''.join(sorted(interested))
# logic behind the anagram program
# ideal case - work with the internal structure (array) with all
# words from the dictionary and try to find proper letters in those words
# it is up to you how you'll handle this area, try to figure this out

# print the requested anagrams
words = load_dict()

words_sorted=[]
for x in words:
    words_sorted.append(''.join(sorted(x)))

i=0
pos=[]
for x,y in enumerate(words_sorted):
    if y == interested_sorted:
        pos.append(x)

print(pos)