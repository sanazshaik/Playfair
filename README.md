# Playfair
Objective: Encrypts an input phrase with set of rules to generate a cipher key using matrices

The program first cleans the string text and removes any white spaces, punctuation, the letter "q" and duplicates. Each string is filled with the remaining letters of the alphabet so that each encrypted phrase has 25 letters.

There are 4 playfair rules that checks bigram inputs (2 letter phrase) and uses matrices to figure out and change the position of a letter. Further details are commented in the program. 

The program goes through test-driven-development by coding a series of test functions to makes sure each of the functions are performing properly without error.
