# bulls and cows
import random
import string

j = random.randint(1,14)
items = ['time', 'most', 'hate', 'rain', 'hand', 'thing', 'open', 'nice', 'fall', 'dear', 'like', 'hurt', 'happy', 'stay']
word = items[j]
t = len(word)

print "         Welcome\n"
print "            To\n"
print "The Game Of Bulls and Cows\n"
print "\nThe rules of the games are: \n1.> You have to guess a word.\n2.> No. of bulls = No.of characters that are common in both.\n3.> No. of cows = No. of characters whose position matches with the position of the guessed word.\n"
print "Go ahead !!\nAll the best\n"

def dash(word):
    print "\nGuess a",t,"letter word: ",
    for char in word:
        print "_",

def bull(word, guess):
    countb = 0
    for char in word:
        if char in guess:
            countb = countb+1

    print "Bulls = ", countb
    return countb
    
def cow (word, guess, t):
    countc = 0
    for i in range (0,t):
        #if word[i] == guess:
        if guess[i] == word[i]:
            countc = countc + 1

    print "Cows = ", countc
    return countc
b = c = 0
    
while b < t or c < t:  
    dash(word)
    guess = raw_input("\n")
    b = bull(word, guess)
    c = cow(word, guess, t)

print "\nCongratulations...!!\nThe word is "+word +"\nThank you for playing.\nBye!"


    
