#import wordgenerator
import wordgenerator

#import the time module
import time

name = input("Enter your name: ")  #**************

print ("Hello, " + name, " Start playing word guessing game")
print ("You have to guess five letters word in 10 guesses")
print (" ")

#wait for 1 second
time.sleep(1)

print ("Start guessing a word game")
time.sleep(0.5)

#get a 5 letter random word 
word = wordgenerator.randomword()
#print(word)               **********
#creates an empty string
guesses = ''

nturns = 10

#check the numbber turns left 
while nturns > 0:         

    # a counter for failure
    failed = 0             

    # fetch a character    
    for char in word:      

    # Check if a character is in  guesses string print it
        if char in guesses:    
    
        
            print( char, end=' '   ) 

        else:
    
        # If no match, print a dash
            print ("_",end=' ')     
       
        # Increase the failed counter by one
            failed += 1    

    # if failed is equal to zero

    
    if failed == 0:        
        print( " \nWow You have won the game!!!"  )

    # exit the script
        break              

    print('\n')

    # Ask player to guess a letter
    guess = input("Guess a character: ") 

    # set the players guess to guesses
    guesses += guess                    

    
    if guess not in word:  
 
     # if the guess is not found decrease nturns counter by 1 
        nturns -= 1        
 
    
        print ("Wrong choice"  )  
 
    # Number of terms left
        print( "You have ", + nturns, ' terms left now' )
 
    # if the nturns are equal to zero
        if nturns == 0:           
    
        
            print ("You Lost the game")
            print("The correct word is ", word)
            

# Run a script
# E:\Python3x>python f:\guessingapp\guessinggame\game.py

# Enter your name? Narayan
# Hello, Narayan  Start playing word guessing game
# You have to guess five letters word in 10 guesses

# Start guessing a word game
# civil
# _ _ _ _ _

# Guess a character: i
# _ i _ i _

# Guess a character: s
# Wrong choice
# You have  9  terms left now
# _ i _ i _

# Guess a character: c
# c i _ i _

# Guess a character: v
# c i v i _

# Guess a character: l
# c i v i l
# Wow You have won the game!!!