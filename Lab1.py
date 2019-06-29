#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 13:29:35 2019
University of Texas at El Paso
CS 2302 - Summer 2019
Author: Dafne Bencomo
Lab 1 - Recursion
Instructor: Olac Fuentes
TA: Ismael Villanueva-Miranda
Last modified: 06/17/2019
Purpose: The purpose of this program is to give a user the anagrams of a word
         of their choice
"""
import time
wordSet = set()
wordSet = open("words_alpha.txt").read().splitlines()

'''
The method 'anagram' receives two strings 'w' and 'scramble', a list 'L' and a 
set 's' as parameters and returns set 's' after calculating all possible 
permutations for 'w', checking how many of them are anagrams and adds them to 
the set
'''
def anagram(w, scramble, words, s):
    if len(w) == 0:
        if scramble in words: #checking to see which permutations are anagrams
            s.add(scramble)
    else:
        for i in range(len(w)):
            chosen = w[i] #chooses letter to begin each permutation word with scramble
            remaining = w[:i] + w[i+1:] #joins the letters in the word that were not the chosen
            anagram(remaining, scramble + chosen, words, s) 
    return s 
 
'''
The method 'search' receives a set 's' as a parameter. It calls the method 
'anagram' and then sorts the list in alphabetical order before printing it.
It also computes and displays the total time it took the program to find the 
anagrams 
'''           

def search(s):
    set1 = set()
    start = time.perf_counter()
    anList = list(anagram(word, '', wordSet, set1)) #converts the set returned into a list
    anList.sort() 
    print('The word ' + word + ' has ' + str(len(anList)) + ' anagrams: ' )
    end = time.perf_counter()
    for i in range(len(anList)):
        print(anList[i]) #prints each anagram in the list
    print('It took ' + str(round((end - start), 6)) + ' seconds to find the anagram(s).\n')

 
word = input("Enter a word or empty string:\n")  
if len(word) > 0 and word.startswith(' ') == False: 
    print('Word: ' + word)    
    search(wordSet)
else:
    print("Bye! Thanks for using the program!")
    