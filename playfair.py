# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 14:59:57 2020

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Sanaz Shaik
"""
# 
from string import ascii_lowercase


def cleanPhrase(phrase): # this helper function converts a string to lowercase and checks if it is in the alphabet and removes all punctuation, q's, and spaces
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    passphrase = ''
    for ch in phrase:
        if ch.lower() in characters:
            passphrase += ch.lower()
    noDuplicates = [] # remove duplicates in passphrase
    for ch in passphrase: 
        if ch not in noDuplicates:
            noDuplicates.append(ch)
            
    output = ''
    if len(noDuplicates) < 25:
        different = list(set(characters) - set(noDuplicates))
        different.sort() # add the rest of alphabet sorted and makes sure it is 25 letters 
            
        for ch in different: # appending rest of letters into passphrase;
            noDuplicates.append(ch)
        output = ''.join(noDuplicates[:25])
    else:
        output = ''.join(noDuplicates[:25])
    return output

def createTable(phrase):
    '''
    Given an input string, create a lowercase playfair table.  The
    table should include no spaces, no punctuation, no numbers, and 
    no Qs -- just the letters [a-p]+[r-z] in some order.  Note that 
    the input phrase may contain uppercase characters which should 
    be converted to lowercase.
    
    Input:   string:         a passphrase
    Output:  list of lists:  a ciphertable
    '''
    output = cleanPhrase(phrase) 
    row = []
    table5x5 = []
    for ch in range(len(output)):
        row.append(output[ch])
        if len(row) == 5:
            table5x5.append(row)
            row = []
    return table5x5

def cleanPlaintext(plaintext): # this helper function sets up splitString() function and make sures the characters are lowercase, contain no punctuation and spaces, and are in the alphabet
    characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    passphrase = []
    for ch in plaintext:
        if ch.lower() in characters:
            passphrase += ch.lower()
    return passphrase
    

def splitString(plaintext):
    '''
    Splits a string into a list of two-character pairs.  If the string
    has an odd length, append an 'x' as the last character.  As with
    the previous function, the bigrams should contain no spaces, no
    punctuation, no numbers, and no Qs.  Return the list of bigrams,
    each of which should be lowercase.
    
    Input:   string:  plaintext to be encrypted
    Output:  list:    collection of plaintext bigrams
    '''
    passphrase = cleanPlaintext(plaintext)
    if len(passphrase) % 2 != 0: # if the length of passphrase is odd, x is added to the end of string
        passphrase.append('x')
    passphrase = ''.join(passphrase) # convert list to string 
    
    bigram = [] # convert string into bigram
    n  = 2
    for ch in range(0, len(passphrase), n):
        bigram.append(passphrase[ch : ch + n])
    return bigram
        

def playfairRuleOne(pair):
    '''
    If both letters in the pair are the same, replace the second
    letter with 'x' and return; unless the first letter is also
    'x', in which case replace the second letter with 'z'.
    
    You can assume that any input received by this function will 
    be two characters long and already converted to lowercase.
    
    After this function finishes running, no pair should contain two
    of the same character   
    
    Input:   string:  plaintext bigram
    Output:  string:  potentially modified bigram
    '''
    if pair[0] == pair[-1]: # checks the first and last character of the pair
        if pair[0] != 'x' :
            x = pair[0] + 'x' # adds 'x' to the end if the first letter is not 'x'
            return x
        else:
            x = pair[0] + 'z' # adds 'z' to the end if the first letter is 'x'
            return x
    else:
        return pair # otherwise return the original pair of conditions arent met
    return x

def playfairRuleTwo(pair, table):
    '''
    If the letters in the pair appear in the same row of the table, 
    replace them with the letters to their immediate right respectively
    (wrapping around to the left of a row if a letter in the original
    pair was on the right side of the row).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
    for i in range(5): # row
        i1, i2 = i, i
        j1, j2 = -1, -1
        for j in range(5): # column 
            if table[i][j] == pair[0]: # first letter
                i1 = i
                j1 = j
            elif table[i][j] == pair[1]: # i and j are the coordinates and checks that of the first pair
                i2 = i
                j2 = j
        if j1 != -1 and j2 != -1: # loops backs in the row if the second character is located at the last position ( j2 == 4 ) and takes the first character of that same row
            if j2 == 4:
                x = table[i1][j1+1]
                y = table[i2][0]
            else:
                x = table[i1][j1+1]
                y = table[i2][j2+1]
            pair = pair[:0] + x + pair[1:] # moves the first given character to the second character
            pair = pair[:1] + y + pair[2:] # moves the second given character to the third character 
            return pair
    return pair


def playfairRuleThree(pair, table):
    '''
    If the letters in the pair appear in the same column of the table, 
    replace them with the letters immediately below respectively
    (wrapping around to the top of a column if a letter in the original
    pair was at the bottom of the column).  Return the new pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''    
    transpose = list()
    for i in range(len(table[0])):
        row = list()
        for ch in table:
            row.append(ch[i])
        transpose.append(row) # takes the first character of each column and turns those letters into the first row... and so on
    return playfairRuleTwo(pair, transpose)
    


def playfairRuleFour(pair, table):
    '''
    If the letters are not on the same row and not in the same column, 
    replace them with the letters on the same row respectively but in 
    the other pair of corners of the rectangle defined by the original 
    pair.  The order is important -- the first letter of the ciphertext
    pair is the one that lies on the same row as the first letter of 
    the plaintext pair.
    
    You can assume that the pair input received by this function will 
    be two characters long and already converted to lowercase, and
    that the Playfair Table is valid.  
    
    Input:   string:         potentially modified bigram
    Input:   list of lists:  ciphertable
    Output:  string:         potentially modified bigram
    '''
    if pair != playfairRuleTwo(pair, table): # checks through rules
        return pair
    elif pair != playfairRuleThree(pair, table):
        return pair 
    
    rowList = []
    myList = []
    for i in pair:
        for row in table:
            if i in row:
                myList.append(row.index(i)) # adding a new pair into mylist
                rowList.append(table.index(row)) # adding a new pair into rowList
                
    x = table[rowList[0]][myList[1]] # adding the position of that row
    y = table[rowList[1]][myList[0]]
    pair = x + y
    return pair 
    

def encrypt(pair, table):
    '''
    Given a character pair, run it through all four rules to yield
    the encrypted version!
    
    Input:   string:         plaintext bigram
    Input:   list of lists:  ciphertable
    Output:  string:         ciphertext bigram
    '''
    a = playfairRuleOne(pair) 
    b = playfairRuleTwo(a, table)
    c = playfairRuleThree(b, table)
    return playfairRuleFour(c, table)
    

def joinPairs(pairsList):
    '''
    Given a list of many encrypted pairs, join them all into the 
    final ciphertext string (and return that string)
    
    Input:   list:    collection of ciphertext bigrams
    Output:  string:  ciphertext
    '''
    ciphertext = ''.join(pairsList) # converts list to string
    return ciphertext


def main():
    '''
    Example main() function; can be commented out when running your
    tests
    '''
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    print("ALL TESTS PASSED!")
    
    
    # print(createTable('i am entering a pass phrase'))
    # print(playfairRuleOne('xx'))
    # print(playfairRuleTwo('pt', [['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z']]))
    # print(playfairRuleThree('th', [['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z']]))
    # print(playfairRuleFour('as', [['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z']] ))
    # print(encrypt('ps', [['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z']] ))
    
    # table = createTable("i am entering a pass phrase")
    # splitMessage = splitString("this is a test message")
    # pairsList = []

    # print(table) # printed for debugging purposes
    
    # for pair in splitMessage:
    #     # Note: encrypt() should call the four rules
    #     pairsList.append(encrypt(pair, table))
    # cipherText = joinPairs(pairsList)    
    
    # print(cipherText) #printed as the encrypted output
    # #output will be hjntntirnpginprnpm


###############################################################

# Here is where you will write your test case functions
    
# Below are the tests for createTable()
def test1():
    # tests whether the function returns a 5x5 list of lists based on a given string
    assert createTable("i am entering a pass phrase") == [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ], "The function did not return a 5x5 ciphertable"
    assert createTable("abcdefghijklmnopqrstuvwxyz") == [ ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'r', 's', 't', 'u'], ['v', 'w', 'x', 'y', 'z'] ], "The function did not remove 'q' and did not return 25 unique characters"
    assert createTable("!.a-b #") == [ ['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'r', 's', 't', 'u'], ['v', 'w', 'x', 'y', 'z'] ], "The function did not remove any punctuation or spaces"
    assert createTable("ssssss") == [ ['s', 'a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h', 'i'], ['j', 'k', 'l', 'm', 'n'], ['o', 'p', 'r', 't', 'u'], ['v', 'w', 'x', 'y', 'z'] ], "The function did not remove any duplicates"

# Below are the tests for splitString()
def test2():
    # tests whether the function correctly takes in a string and return a bigram list
    assert splitString("this is my plaintext") == ["th", "is", "is", "my", "pl", "ai", "nt", "ex", "tx"], " The function did not append an 'x' to the string"
    assert splitString("this is my plaintex") == ["th", "is", "is", "my", "pl", "ai", "nt", "ex"], "The string is even and the function did not split the string by two"
    assert splitString("yes") != ["y", "e", "s", "x"], " The function did not return a list that has a pair of characters"
    assert splitString("this is my plaintext!") == ["th", "is", "is", "my", "pl", "ai", "nt", "ex", "tx"], " The function did not remove punctuation"

# Below are the tests for playfairRuleOne()
def test3():
    # tests whether the function returns a pair of character and its correct replacement
    assert playfairRuleOne('aa') == 'ax', " The function did not replace the second character with an 'x'"
    assert playfairRuleOne('xx') == 'xz', " The function did not replace the second character with an 'z'"
    assert playfairRuleOne('ab') == 'ab', " The function replaced characters"
    assert playfairRuleOne('cx') == 'cx', " The function replaced characters"

# Below are the tests for playfairRuleTwo()
def test4():
    # tests whether the function returns the correct characters replaced
    assert playfairRuleTwo('am', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'me', " The function did not replace the correct pair"
    assert playfairRuleTwo('pt', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'sr', " The function did not replace the correct pair"
    assert playfairRuleTwo('cf', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'dh', " The function did not replace the correct pair"
    assert playfairRuleTwo('ed', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'ed', " The function should return the same input pir"

# Below are the tests for  playfairRuleThree()
def test5():
    # tests whether the function returns the correct characters replaced
    assert playfairRuleThree('th', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'hj', " The function did not replace the correct characters"
    assert playfairRuleThree('lg', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'xc', " The function did not replace the correct characters"
    assert playfairRuleThree('tv', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'hi', " The function did not replace the correct characters"
    assert playfairRuleThree('ax', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'ax', " The function should return the same input pair"

# Below are the tests for playfairRuleFour()
def test6():
    # tests whether the function returns the correct characters replaced
    assert playfairRuleFour('fm', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'cn', " The function did not replace the correct characters"
    assert playfairRuleFour('as', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'nr', " The function did not replace the correct characters"
    assert playfairRuleFour('jw', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'kv', " The function did not replace the correct characters"
    assert playfairRuleFour('do', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'do', " The function should return the same input pair"

# Below are the tests for encrypt()
def test7():
    # tests whether the function properly encrypt a pair of characters using the four of the playfair rules
    assert encrypt('gg', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'cm', " The function did not encrypt the correct characters"
    assert encrypt('gg', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) != 'gx', " The function did not pass through playfairRuleThree() and playfairRuleFour()"
    assert encrypt('ps', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) == 'st', " The function did not encrypt the correct characters"
    assert encrypt('ps', [ ['i', 'a', 'm', 'e', 'n'], ['t', 'r', 'g', 'p', 's'], ['h', 'b', 'c', 'd', 'f'], ['j', 'k', 'l', 'o', 'u'], ['v', 'w', 'x', 'y', 'z'] ]) != 'sx', " The function did not encrypt the correct characters"

# Below are the tests for joinPairs()
def test8():
    # tests whether the function correctly converts a list of bigram into a string in the correct order
    assert joinPairs(['go', 'ld']) == "gold", " The function did not convert a bigram into a string"
    assert joinPairs(['hj', 'nt', 'nt', 'ir', 'np', 'gi', 'no', 'rn', 'pm']) == "hjntntirnpginprnpm", " The function did not convert a bigram into a string"
    assert joinPairs(['mi', 'ce']) == "mice", " The function did not convert a list into a string"
    assert joinPairs(['dl', 'og']) != "gold", " The function converted a lbigram into a string in the wrong order"
    
###############################################################    
    
if __name__ == "__main__":
    main()        